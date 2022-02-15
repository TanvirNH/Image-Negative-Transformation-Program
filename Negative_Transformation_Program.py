"""
Copyright 2022 Tanvir N Hasan
Licensed under the GNU General Public License, Version 3.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
https://www.gnu.org/licenses/gpl-3.0.en.html
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

"""
from PIL import Image
from PIL import ImageFilter
from matplotlib import pyplot as graph

input_image = str(input("Please Input the name of the image file (put .jpg or .png at the end of the file name): "))

image1 = Image.open(input_image)
image2 = Image.open(input_image)

colour_model = 255 #Colour = White
for i in range(0, image1.size[0]):
    for j in range(0, image1.size[1]):
        all_colours = image1.getpixel((i,j))
        R = colour_model - all_colours[0]
        G = colour_model - all_colours[1]
        B = colour_model - all_colours[2]
        image1.putpixel((i,j),(R, G, B))

graph.figure(num="Negative Transformation Image")
graph.subplot(121),graph.imshow(image2)
graph.title('Input Image:'), graph.xticks([]), graph.yticks([])
graph.subplot(122),graph.imshow(image1)
graph.title('Altered Image:'), graph.xticks([]), graph.yticks([])
graph.show()