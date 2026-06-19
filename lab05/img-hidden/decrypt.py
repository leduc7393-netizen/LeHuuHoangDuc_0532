import sys
from PIL import Image

def decode_image(encoded_image_path):
    img = Image.open(encoded_image_path)
    width, height = img.size
    binary_message = ""
    
    # Trích xuất các bit cuối cùng (LSB) từ mỗi kênh màu của pixel
    for row in range(height):
        for col in range(width):
            pixel = img.getpixel((col, row))
            
            for color_channel in range(3):
                binary_message += format(pixel[color_channel], '08b')[-1]
    
    # Chuyển đổi nhị phân thành ký tự
    message = ""
    for i in range(0, len(binary_message), 8):
        # Lấy từng khối 8 bit
        byte = binary_message[i:i+8]
        char = chr(int(byte, 2))
        
        # Dừng lại nếu gặp ký tự null (dấu hiệu kết thúc đã quy định trong code mã hóa)
        if char == '\0':
            break
        message += char
        
    return message

def main():
    if len(sys.argv) != 2:
        print("Usage: python decrypt.py <encoded_image_path>")
        return
    
    encoded_image_path = sys.argv[1]
    decoded_message = decode_image(encoded_image_path)
    print("Decoded message:", decoded_message)

if __name__ == "__main__":
    main()