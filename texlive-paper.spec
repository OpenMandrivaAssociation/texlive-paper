# revision 25802
# category Package
# catalog-ctan /macros/latex/contrib/paper
# catalog-date 2012-01-13 09:08:17 +0100
# catalog-license gpl
# catalog-version 1.0l
Name:		texlive-paper
Version:	1.0l
Release:	10
Summary:	Versions of article class, tuned for scholarly publications
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/paper
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/paper.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/paper.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/paper.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Fri Apr 13 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0l-4
+ Revision: 790732
- Update to latest release.

* Thu Jan 19 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0l-3
+ Revision: 762692
- Update to latest upstream package

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0l-2
+ Revision: 754637
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0l-1
+ Revision: 719185
- texlive-paper
- texlive-paper
- texlive-paper
- texlive-paper

