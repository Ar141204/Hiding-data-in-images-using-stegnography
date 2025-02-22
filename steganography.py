from PIL import Image
import binascii
import optparse

def rgb2hex(r, g, b):
    return '{:02x}{:02x}{:02x}'.format(r, g, b)

def hex2rgb(hex):
    return tuple(int(hex[i:i+2], 16) for i in range(0, 6, 2))

def str2bin(message):
    binary = bin(int(binascii.hexlify(message.encode()), 16))
    return binary[2:]

def bin2str(binary):
    message = binascii.unhexlify('%x' % (int('0b' + binary, 2)))
    return message.decode()

def encode(hex, digit):
    if hex[-1] in '0123456789abcdef':
        hex = hex[:-1] + digit
        return hex
    else:
        return None

def decode(hex):
    if hex[-1] in '0123456789abcdef':
        return hex[-1]
    else:
        return None

def hide_data(image_path, message, output_path):
    image = Image.open(image_path)
    binary_message = str2bin(message) + '1111111111111110'
    if image.mode in 'RGBA':
        image = image.convert('RGBA')
        data = image.getdata()
        new_data = []
        digit = 0
        temp = ''
        for item in data:
            if digit < len(binary_message):
                newpix = encode(rgb2hex(item[0], item[1], item[2]), binary_message[digit])
                if newpix:
                    r, g, b = hex2rgb(newpix)
                    new_data.append((r, g, b, 255))
                    digit += 1
                else:
                    new_data.append(item)
            else:
                new_data.append(item)
        image.putdata(new_data)
        image.save(output_path, "PNG")
        return "Message encoded successfully!"
    return "Incorrect Image Mode, Couldn't Hide"

def retr_data(image_path):
    image = Image.open(image_path)
    binary = ''
    if image.mode in 'RGBA':
        image = image.convert('RGBA')
        data = image.getdata()
        for item in data:
            digit = decode(rgb2hex(item[0], item[1], item[2]))
            if digit:
                binary = binary + digit
                if binary[-16:] == '1111111111111110':
                    return bin2str(binary[:-16])
        return bin2str(binary)
    return "Incorrect Image Mode, Couldn't Retrieve"

def main():
    parser = optparse.OptionParser('usage %prog ' + '-e/-d <target file>')
    parser.add_option('-e', dest='hide', type='string', help='target picture path to hide text')
    parser.add_option('-d', dest='retr', type='string', help='target picture path to retrieve text')
    parser.add_option('-m', dest='message', type='string', help='message to hide')
    parser.add_option('-o', dest='output', type='string', help='output picture path')
    (options, args) = parser.parse_args()
    if options.hide and options.message and options.output:
        print(hide_data(options.hide, options.message, options.output))
    elif options.retr:
        print(retr_data(options.retr))
    else:
        print(parser.usage)
        exit(0)

if __name__ == '__main__':
    main()
