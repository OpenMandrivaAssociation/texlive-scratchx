%global tl_name scratchx
%global tl_revision 44906

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	Include Scratch programs in LaTeX documents
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/scratchx
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/scratchx.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/scratchx.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package can be used to include every kind of Scratch program in
LaTeX documents. This may be particularly useful for Math Teachers and
IT specialists. The package depends on the following other LaTeX
packages: calc, fp, ifsym, multido, tikz, xargs, and xstring.

