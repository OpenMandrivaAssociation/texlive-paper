%global tl_name paper
%global tl_revision 79461

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0l
Release:	%{tl_revision}.1
Summary:	Versions of article class, tuned for scholarly publications
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/paper
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/paper.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/paper.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/paper.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A pair of classes derived from article, tuned for producing papers for
journals. The classes introduce new layout options and font commands for
sections/parts, and define a new keywords environment, subtitle and
institution commands for the title section and new commands for
revisions.

