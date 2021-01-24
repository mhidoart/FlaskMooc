from fpdf import FPDF


class PDF(FPDF):
    pass  # nothing happens when it is executed.


class Pdf_writer:

    def __init__(self, file):
        self.target = file
        self.pdf = PDF()

    def get_target(self):
        return str(self.target)

    def write_line(self, line, font='Arial', size=14):

        # Begin with regular font
        self.pdf.set_font(font, '', size)
        if(not str(line).endswith('\n')):
            line += '\n'
        self.pdf.write(5, line)
        # Then put a blue underlined link
        #pdf.set_text_color(0, 0, 255)
        #pdf.set_font('', 'U')

    def add_page(self):
        self.pdf.add_page()

    def save(self):
        if(not str(self.target).endswith('.pdf')):
            self.target += '.pdf'

        self.pdf.output(self.target, 'F')
# if u want to test this module


'''
writer = Pdf_writer('assabbane')
writer.add_page()
writer.write_line('hello')
writer.write_line('word!')
writer.save()
'''
