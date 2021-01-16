from utilities import comma_seperate_list
from jinja2 import Template


class Module:
    """
    Class representing a course module. Usually initialized with a json read.
    Keyword arguments:
        name - a string for the name of the module
        readings - a list of assigned readings usually chapter.section numbers (Ex: [2.1, 2.2])
        advice - a list of strings, possibly containing latex code
        work - a dictionary with 'chapter.section':'string of problems' the problem string is assumed to be formatted
    """

    def __init__(self, name='', videos={}, readings=[], advice=[], work={}):
        self.name = name
        self.videos = videos
        self.readings = readings
        self.advice = advice
        self.work = work

    # the two major methods are latex and html
    def latex(self, file, index):
        """
        Latex code generation, writes tex code for the module assuming that the module is week index.
        Helper functions include tab generation to create readable code.
        Arguments:
            file - a file stream for the output
            index - integer for the week of the module
        """
        self.header_latex(file, index)
        if self.readings:
            self.readings_latex(file)
        if self.advice:
            self.advice_latex(file)
        if self.work:
            self.work_latex(file)
        self.footer_latex(file, index)

    def html(self, file, index):
        """
        HTML code generation, writes html code for the module assuming that the module is week index.
        Helper functions include tab generation to create readable code.
        Note, the latex code in the advice section will not render automatically with html at this time.
        Arguments:
            file - a file stream for the output
            index - integer for the week of the module
        """
        self.header_html(file, index)
        if self.videos:
            self.videos_html(file)
        if self.readings:
            self.readings_html(file)
        if self.advice:
            self.advice_html(file)
        if self.work:
            self.work_html(file)
        self.footer_html(file, index)

    def html_template(self, file, index):
        """
        HTML code generation using template, writes html code for the module assuming that the module is week index.
        Note, the latex code in the advice section will not render automatically with html at this time.
        Arguments:
            file - a file stream for the output
            index - integer for the week of the module
        """
        # Read the raw template
        with open('templates/module.html', 'r') as f:
            string = f.read()

        # Convert to jinja2 template
        template = Template(string, trim_blocks=True, lstrip_blocks=True)

        # Render the template
        x = template.render(obj=self, i=index)

        # Print to the target file
        print(x, file=file)

    def header_latex(self, file, index):
        """Helper function for latex method. Generates header."""
        print("% <------------" + f"{self.name} Begins Here" + "------------>\n", file=file)
        print('\t' + r"\section{Week " + f"{index} - {self.name}" + "}\n", file=file)

    def footer_latex(self, file, index):
        """Helper function for latex method. Generates footer."""
        print('\t' + r"\clearpage" + '\n', file=file)
        print("% <------------" + f"{self.name} Ends Here" + "------------>\n", file=file)

    def readings_latex(self, file):
        """Helper function for latex method. Generates readings statement."""
        # readings header
        print('\t' + r"\subsection{Readings}", file=file)
        # readings statement
        print('\t' * 2 + f"Please read sections {comma_seperate_list(self.readings)}." + '\n', file=file)

    def advice_latex(self, file):
        """Helper function for latex method. Generates itemized advice."""
        # advice header
        print('\t' + r"\subsection{Words of Advice}", file=file)
        # itemized advice
        print('\t' * 2 + r"\begin{itemize}", file=file)
        for item in self.advice:
            print('\t' * 3 + r"\item " + item, file=file)
        print('\t' * 2 + r"\end{itemize}" + '\n', file=file)

    def work_latex(self, file):
        """Helper function for latex method. Generates itemized work assignments."""
        # work header
        print('\t' + r"\subsection{Work}", file=file)
        # itemized work list
        print('\t' * 2 + r"\begin{itemize}", file=file)
        for key, value in self.work.items():
            print('\t' * 3 + r"\item " + f"In section {key}, please do problems {value}.", file=file)
        print('\t' * 2 + r"\end{itemize}" + '\n', file=file)

    def header_html(self, file, index):
        """Helper function for html method. Generates header."""
        print(f'<!-- Module {index} - {self.name} Begins Here -->', file=file)
        print(f"<h2>Week {index} - {self.name}</h2>\n", file=file)

    def footer_html(self, file, index):
        """Helper function for html method. Generates footer."""
        print(f'<!-- End of Module {index} -->', file=file)

    def videos_html(self, file):
        """Helper function for html method. Generates itemized video links."""
        # videos header
        print("\t<h3>Videos</h3>", file=file)
        # itemized video link list
        print('\t' * 2 + "<ul>", file=file)
        for name, link in self.videos.items():
            print('\t' * 3 + f"<li><a class=\"inline_disabled\" href=\"{link}\">{name}</a></li>", file=file)
        print('\t' * 2 + "</ul>\n", file=file)

    def readings_html(self, file):
        """Helper function for html method. Generates readings statement."""
        # readings header
        print("\t<h3>Readings</h3>", file=file)
        # readings statement
        print('\t' * 2 + f"<p>Please read sections {comma_seperate_list(self.readings)}.</p>\n", file=file)

    def advice_html(self, file):
        """Helper function for html method. Generates itemized advice."""
        # advice header
        print("\t<h3>Words of Advice</h3>", file=file)
        # itemized advice
        print('\t' * 2 + "<ul>", file=file)
        for item in self.advice:
            print('\t' * 3 + f"<li>{item}</li>", file=file)
        print('\t' * 2 + "</ul>\n", file=file)

    def work_html(self, file):
        """Helper function for html method. Generates itemized work assignments."""
        # work header
        print("\t<h3>Work</h3>", file=file)
        # itemized work list
        print('\t' * 2 + "<ul>", file=file)
        for key, value in self.work.items():
            print('\t' * 3 + f"<li>In section {key}, please do problems {value}.</li>", file=file)
        print('\t' * 2 + "</ul>\n", file=file)
