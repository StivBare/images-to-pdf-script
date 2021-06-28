from fpdf import FPDF
import glob


def pdfMaker(title):
    class PDF(FPDF):
        def header(self):
            self.set_font('Arial', 'B', 15)
            self.cell(80)
            self.cell(30, 10, title, 0, 0, 'C')
            self.ln(20)

    pdf = PDF()
    imagelist = glob.glob("") #uploaded images
    save_path = ""
    pdf.add_page()
    pdf.set_title(title)

    x = 10 #abscissa of upper-left corner
    y = 35 #ordinate of upper-left corner
    j = 0 #number of pictures on column
    m = 0 #number of rows on page


    # pdf pixel width: 210
    # pdf pixel height: 297

    for image in imagelist:
        pdf.rect(x - 0.7, y-0.7, 56.4, 46.4) #create border around images
        pdf.image(image, x, y, 55, 45)
        j = j + 1
        x += 67.5
        if j == 3: #add row at 3 pictures per column
            y = y + 57
            x = 10
            j = 0
            m += 1
            if m == 4: #stop at 4 rows
                pdf.add_page() #create another page and reset pixel count
                m = 0
                x = 10
                y = 35

    pdf.output(save_path + "example1.pdf", "F")


pdfMaker("Example")


