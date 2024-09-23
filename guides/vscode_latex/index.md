# Setting Up VSCode for Writing LaTeX Documents

This guide will walk you through setting up Visual Studio Code (VSCode) for writing LaTeX documents on Windows, Mac, and Linux. It includes the necessary downloads, recommended extensions, and an example file structure.

## Downloads and Installation

### Windows

1. **Install VSCode**: Download and install VSCode from [here](https://code.visualstudio.com/).

2. **Install MiKTeX**:
   - Download MiKTeX from [here](https://miktex.org/download).
   - Run the installer and follow the on-screen instructions.

3. **Install Perl** (required for `latexindent`):
   - Download Strawberry Perl from [here](http://strawberryperl.com/).
   - Run the installer and follow the on-screen instructions.

### Mac

1. **Install VSCode**: Download and install VSCode from [here](https://code.visualstudio.com/).

2. **Install MacTeX**:
   - Install MacTeX using Homebrew:

     ```sh

     brew install --cask mactex

     ```

3. **Install Required Perl Modules**:
   - Open Terminal and run:

     ```sh

     sudo cpan Log::Log4perl File::HomeDir YAML::Tiny

     ```

### Linux

1. **Install VSCode**: Follow the instructions [here](https://code.visualstudio.com/docs/setup/linux) to install VSCode for your specific Linux distribution.

2. **Install TeX Live**:
   - Install TeX Live using your package manager. For example, on Ubuntu:

     ```sh

     sudo apt-get install texlive-full

     ```

3. **Install Perl Modules**:
   - Install the required Perl modules:

     ```sh

     sudo cpan Log::Log4perl File::HomeDir YAML::Tiny

     ```

## VSCode Extensions

Install the following extensions in VSCode for a better LaTeX editing experience:

1. **LaTeX Workshop**: Provides comprehensive LaTeX support including build process management, PDF viewing, and more.
   - Search for "LaTeX Workshop" in the Extensions view and install it.

2. **Markdown All in One**: Enhances Markdown editing with features like auto-preview and shortcuts.
   - Search for "Markdown All in One" in the Extensions view and install it.

3. **Spell Right**: Spell checking extension for VSCode.
   - Search for "Spell Right" in the Extensions view and install it.

4. **Zotero Integration**: For managing citations from Zotero.
   - Search for "Zotero Integration" in the Extensions view and install it.

5. **BibTeX Utilities**: Provides support for managing BibTeX files.
   - Search for "BibTeX Utilities" in the Extensions view and install it.

## Setting Up an Example File Structure

Here’s a suggested directory structure for organising your LaTeX projects:

```sh

project_root/
│
├── shared/
│   ├── styles/
│   │   ├── custom.sty
│   │   └── other_styles.sty
│   ├── templates/
│   │   └── template.tex
│   └── bibliography/
│       └── references.bib
│
├── document1/
│   ├── figures/
│   ├── images/
│   ├── sections/
│   ├── code/
│   ├── document1.tex
│   └── Makefile
│
└── document2/
    ├── figures/
    ├── images/
    ├── sections/
    ├── code/
    ├── document2.tex
    └── Makefile

```

### Example `document1.tex` Using Shared Resources

```latex
\documentclass{article}
\usepackage{../shared/styles/custom}
\usepackage{../shared/styles/other_styles}
\bibliography{../shared/bibliography/references}

\begin{document}
\title{Document 1}
\author{Author Name}
\date{\today}
\maketitle

\section{Introduction}
This is an introduction.

\input{sections/introduction}

\section{Methods}
This is the methods section.

\input{sections/methods}

\section{Results}
This is the results section.

\input{sections/results}

\section{Conclusion}
This is the conclusion.

\input{sections/conclusion}

\bibliographystyle{plain}
\bibliography{../shared/bibliography/references}
\end{document}
```

## Commands to Verify Installation

### Verify LaTeX Installation

After installing the required LaTeX distribution (MiKTeX, MacTeX, or TeX Live), verify the installation by running the following commands in your terminal:

```sh
pdflatex --version
latexmk --version
latexindent --version
```

### Verify Perl Installation (Windows)

Check if Perl is installed correctly by running:

```sh

perl -v

```

### Verify Perl Modules (Mac/Linux)

Check if the required Perl modules are installed by running:

```sh

perl -MLog::Log4perl -e 1
perl -MFile::HomeDir -e 1
perl -MYAML::Tiny -e 1

```

If there are no errors, the modules are installed correctly.

## Configuring VSCode LaTeX Workshop

1. Open VSCode and go to File > Preferences > Settings.
2. Search for latex-workshop.latex.tools and add the following configuration:

```json

"latex-workshop.latex.tools": [
  {
    "name": "latexmk",
    "command": "latexmk",
    "args": [
      "-synctex=1",
      "-interaction=nonstopmode",
      "-file-line-error",
      "-pdf",
      "%DOC%"
    ]
  },
  {
    "name": "latexindent",
    "command": "latexindent",
    "args": [
      "-w",
      "%DOC%"
    ]
  }
]

```

To see a real project complete with templates and shared styling check out my GitHub.