# spread2page
Batch convert *consistently* aligned photos of a book in spread format (2-up) into compact individual page image files suitable for pdf eReading.

## input image prereqs
 - align your book reasonably square (try ficing it in place)
 - keep it reasonably flat for photographing (a piece of glass or perspex helps)
 - fix the camera using a tripod or mount, make sure it is squarely facing the book
 - consistent lighting (no falloff or gradients across pages, or shadows
 - sequential file naming, the hardcoded pattern here is `P00001`,`P00002` jpg or png
 
## args 
Rather than doing command line arg, just dive into the code directly to change as needed

## input
<img width="600px" src="https://user-images.githubusercontent.com/3287519/93689199-2c198900-fa9a-11ea-9b82-e855d99eaf8a.jpg" />

input file naming: P00001.[png|jpg] incrementing by one per file padded to 5 digits
```
dx,dx = pixel offset from top right of image to top right corner of page
page_width = of a single page from dx to gutter (valley) between the 2 pages
page_height = from top to bottom of page
image_count = number of images(each of which shows 2 pages)
total_pixel_shift = a measure of the amount the pages move from right to left as the book is paged-through (for thick books)

INPUT_IMAGE_FILETYPE = [png|jpg]
```

## output
<img width="200px" src="https://user-images.githubusercontent.com/3287519/93689227-62ef9f00-fa9a-11ea-9dce-723af4a21c87.jpg" />

Actually two files would be output for the input 2-up image above, here is one:
```
GAMMA = 1.0 (<1.0 darkens the mid-greys)
CONTRAST = 1.0 (>1.0 increases contrast)
JPEG_QUALITY = 30 (0-100, 30 is a good starting point for reasonable file size)
```

## future features
This is bare bones for getting the job done, some other things to add would be:
 - local contrast enhancement
 - page corner detection
 - page outline detenction
 - dewarping using a model of page bend
 - flexible file naming
 - gutter and margin specification
 - ability to use a single quantum-entangled lightfield photo of a book's cover to extrapolate content even when closed

