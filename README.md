# Tetris Mosiac Generator
The project takes in any user image and make a Mosiac-like version where all pixels are made of valid colored Tetris pieces.

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running, download Python3 and change the input image at the top of main.py. There are other parameters
you can change to change the image, but be weary that some may cause long wait times. Running main.py will output an output bmp file that has the same name as the input file, but prefixed with "output_".

### Prerequisites

You will only need very common Python modules to run the program.
* PIL
* Numpy
* Random

## How It's Made:
The project effectively plays a very large game of Tetris first before doing simple image processing. Playing a very large game of Tetris, however, is very difficult. The program is pretty Naive, generating a random piece in a random spot and placing it as low as possible. It then checks for if any "holes" and the "roughness metric". Both of these terms are kinda made up by me. A hole is any space with a block both beneath and above it, and the "roughness metric" is the difference in heights between adjacent columns. Both of these values are kept very low to zero for purely aesthic purposes. Technically you could fill a whole board with only the straight "I" piece, but that would look unappealing, so we check for roughness. This obviously slows down stacking a bit, but I believe the end result is worth it. We then have a very large game of Tetris with the board almost entirely filled, then we take the average of all the pixels contained in each piece. The piece is then colored to that average. The average is a very simple arithimetic mean of the RGB values. The final image is then saved as a BMP file to minimize compression artifacts that distort and blend the pieces. 

<!-- LICENSE -->
## License

Distributed under the MIT License. 


<!-- CONTACT -->
## Contact

Email - kevinlyvers@gmail.com

Personal Website: [www.kevinlyvers.com](www.kevinlyvers.com)
