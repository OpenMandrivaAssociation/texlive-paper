Name:		texlive-paper
Version:	34521
Release:	2
Summary:	Versions of article class, tuned for scholarly publications
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/paper
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/paper.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/paper.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/paper.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A pair of classes derived from article, tuned for producing
papers for journals. The classes introduce new layout options
and font commands for sections/parts, and define a new keywords
environment, subtitle and institution commands for the title
section and new commands for revisions.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/paper/journal.cls
%{_texmfdistdir}/tex/latex/paper/journal.sty
%{_texmfdistdir}/tex/latex/paper/paper.cls
%{_texmfdistdir}/tex/latex/paper/paper.sty
%doc %{_texmfdistdir}/doc/latex/paper/README
%doc %{_texmfdistdir}/doc/latex/paper/install
%doc %{_texmfdistdir}/doc/latex/paper/journal1.tex
%doc %{_texmfdistdir}/doc/latex/paper/journal2.tex
%doc %{_texmfdistdir}/doc/latex/paper/local.tex
%doc %{_texmfdistdir}/doc/latex/paper/paper.pdf
%doc %{_texmfdistdir}/doc/latex/paper/testj.tex
%doc %{_texmfdistdir}/doc/latex/paper/testp.tex
#- source
%doc %{_texmfdistdir}/source/latex/paper/paper.drv
%doc %{_texmfdistdir}/source/latex/paper/paper.dtx

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
