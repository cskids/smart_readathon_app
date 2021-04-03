import cv2
from pyzbar import pyzbar

def read_barcodes(frame):
    barcodes = pyzbar.decode(frame)
    barcode_info = ''
    for barcode in barcodes:
        x, y, w, h = barcode.rect

        barcode_info = barcode.data.decode('utf-8')
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, barcode_info, (x + 6, y - 6), font, 2.0, (255, 255, 255), 1)
    return frame, barcode_info

def get_barcode():
    #1
    camera = cv2.VideoCapture(0)
    ret, frame = camera.read()
    #2
    barcode_info = ''
    while ret:
        ret, frame = camera.read()
        frame, barcode_info = read_barcodes(frame)
        cv2.imshow('Barcode/QR code reader', frame)
        if (cv2.waitKey(1) & 0xFF == 27) or len(barcode_info) >= 10: # Press ESC key to exit
            break
    #3
    camera.release()
    cv2.destroyAllWindows()
    return barcode_info

if __name__ == '__main__':
    isbn = get_barcode()
    print(isbn)
