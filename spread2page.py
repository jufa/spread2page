import numpy as np
import cv2
import math

'''
Convert PNG or JPG photos or scans of page spreads of a book
input image of book 'spread'. Format file name "P00001.png" incrementing with fixed filename length, padded zero
output: JPG grayscale, processed and cropped
'''
def main(argv):
  src_dir = "raw"
  tgt_dir = "processed"
  image_count = 254 # number of 2-page spread images
  dx = 770 # pixels inset from left to top left corner of book
  dy = 404 # pixel inset fromm top to top left corner of book
  page_width = 1094 # pixel width of each page (remember, two pages in each image since we are imaging a 'spread')
  page_height = 1684
  total_pixel_shift = 100.0 # as a books pages are openned, the portion of the image they take up tends to move from left to right. set this to the number of pixels the page spread has shifted from the first page to the last
  pixel_offset_per_image = total_pixel_shift/image_count 
  current_page_index = 1
  current_image_number = 1
  INPUT_IMAGE_FILETYPE = "png" # | "jpg"
  JPEG_QUALITY = 30 # generally a good number for keeping page size down
  CONTRAST_ENHANCE = 1.2 #1.0 is no change, >1 is increased contrast
  GAMMA = 1.0

  def adjust_gamma(image, gamma=1.0):
    # build a lookup table mapping the pixel values [0, 255] to
    # their adjusted gamma values
    invGamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** invGamma) * 255
      for i in np.arange(0, 256)]).astype("uint8")
    # apply gamma correction using the lookup table
    return cv2.LUT((image).astype(np.uint8), table)

  def process_image_to_page(img):
    page = img * CONTRAST_ENHANCE
    ret, page = cv2.threshold(page,255,255,cv2.THRESH_TRUNC)
    page = adjust_gamma(page, GAMMA)
    return page

  for current_image_number in range(1, image_count+1):
    file_name = 'P' + str(current_image_number).zfill(5) + '.' + INPUT_IMAGE_FILETYPE

    print('processing ' + file_name)

    img = cv2.imread(src_dir + '/' + file_name, cv2.IMREAD_GRAYSCALE)

    offset_due_to_progress = current_image_number * pixel_offset_per_image
    y0 = dy
    y1 = y0 + page_height
    x0 = dx + round(offset_due_to_progress)
    x1 = x0 + page_width
    page_left = process_image_to_page(img[y0:y1, x0:x1])

    x0 = x1
    x1 = x1 + page_width
    page_right = process_image_to_page(img[y0:y1, x0:x1])

    file_name_left_page = str(current_image_number * 2 - 1).zfill(5) + ".jpg"
    file_name_right_page = str(current_image_number * 2).zfill(5) + ".jpg"

    cv2.imwrite(tgt_dir + '/' + file_name_left_page, page_left, [cv2.IMWRITE_JPEG_QUALITY, JPEG_QUALITY])
    cv2.imwrite(tgt_dir + '/' + file_name_right_page, page_right, [cv2.IMWRITE_JPEG_QUALITY, JPEG_QUALITY])

    
  print('COMPLETED')

if __name__ == "__main__":
  main(sys.argv[1:])



