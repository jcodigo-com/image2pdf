#Cambiar formato PDF
import glob
from fpdf import FPDF
from PIL import Image
imagelist = glob.glob('distribucion de alimentos 6° dotacion/*.png')

for image in imagelist:
    nombre_archivo = image.replace('.png', '.pdf')
    pdf = FPDF()
    #pdf.add_page()
    #pdf.image(image, 0,0,0)

    cover = Image.open(image)
    width, height = cover.size
    width, height = float(width * 0.264583), float(height * 0.264583)
    pdf_size = {'P': {'w': 210, 'h': 297}, 'L': {'w': 297, 'h': 210}}
    orientation = 'P' if width < height else 'L'
    width = width if width < pdf_size[orientation]['w'] else pdf_size[orientation]['w']
    height = height if height < pdf_size[orientation]['h'] else pdf_size[orientation]['h']
    pdf.add_page(orientation=orientation)
    pdf.image(image, 0, 0, width, height)
    
    pdf.output("PDF/"+nombre_archivo, "F")
