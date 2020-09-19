# spread2page
Batch convert consistently aligned photos of a book in spread format (2-up) into compact individual page image files.
Rather than doing command line arg, just dive into the code directly to change as needed

This is bare bones for getting the job done, some other things to add would be:
 - local contrast enhancement
 - page corner detection
 - page outline detenction
 - dewarping using a model of page bend
 - flexible file naming

## input
input file naming: P00001.[png|jpg] incrementing by one per file padded to 5 digits
```
dx,dx pixel offset from top right of image to top right corner of page
page_width of a single page from dx to gutter (valley) between the 2 pages
page_height from top to bottom of page
image_count - number of images(each of which show 2 pages)

INPUT_IMAGE_FILETYPE = [png|jpg]
```
<img width="600px" src="https://user-images.githubusercontent.com/3287519/93689199-2c198900-fa9a-11ea-9b82-e855d99eaf8a.jpg" />

## output
Actually two files would be output for the input 2-up image above, here is one:
```
GAMMA = 1.0 (<1.0 darkens the mid-greys)
CONTRAST = 1.0 (>1.0 increases contrast)
JPEG_QUALITY = 30 (0-100, 30 is a good starting point for reasonable file size)
```
<img width="200px" src="https://user-images.githubusercontent.com/3287519/93689227-62ef9f00-fa9a-11ea-9dce-723af4a21c87.jpg" />




