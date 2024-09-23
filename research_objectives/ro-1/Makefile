# Define the name of the main LaTeX file without the .tex extension
MAIN = index

# Define the bibliography file without the .bib extension
BIB = ../../shared/bibliography/references

# Define the PDF viewer command
PDFVIEW = open

# The default target is 'all'
all: mermaid_diagrams $(MAIN).pdf

# Rule to build the PDF from the LaTeX file using LaTeX directly
$(MAIN).pdf: $(MAIN).tex $(MAIN).bib
	pdflatex $(MAIN).tex
	bibtex $(MAIN)
	pdflatex $(MAIN).tex
	pdflatex $(MAIN).tex


# Rule to generate PDF from Mermaid file
%.pdf: %.mmd
	mmdc -i $< -o $@

# Rule to generate all Mermaid diagrams
mermaid_diagrams: $(patsubst %.mmd,%.pdf,$(wildcard mermaid/*.mmd))

# Rule to clean auxiliary files
clean:
	rm -f *.aux *.bbl *.blg *.log *.out *.toc *.blg *.dvi *.fdb_latexmk *.fls *.lof *.lot *.synctex.gz

# Rule to open the PDF with the default PDF viewer
view: $(MAIN).pdf
	$(PDFVIEW) $(MAIN).pdf


.PHONY: all clean view mermaid_diagrams
