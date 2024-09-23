# Define the name of the main LaTeX file without the .tex extension
MAIN = $(MAIN)

# Define the bibliography file without the .bib extension
BIB = ../../shared/bibliography/references

# Define the PDF viewer command
PDFVIEW = open

# Rule to open the PDF with the default PDF viewer
view: $(MAIN).pdf
	$(PDFVIEW) $(MAIN).pdf

# Makefile

# Default rule
all: $(MAIN).xetex

# Rule for pdfLaTeX
pdf:
    pdflatex $(MAIN).tex
    bibtex $(MAIN)
    pdflatex $(MAIN).tex
    pdflatex $(MAIN).tex

# Rule for XeLaTeX
xetex:
    xelatex $(MAIN).tex
    bibtex $(MAIN)
    xelatex $(MAIN).tex
    xelatex $(MAIN).tex

# Rule for LuaLaTeX
luatex:
    lualatex $(MAIN).tex
    bibtex $(MAIN)
    lualatex $(MAIN).tex
    lualatex $(MAIN).tex

# Clean up auxiliary files
clean:
    rm -f *.aux *.bbl *.blg *.log *.out *.toc *.fdb_latexmk *.fls *.synctex.gz