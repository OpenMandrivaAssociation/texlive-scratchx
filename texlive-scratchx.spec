Name:		texlive-scratchx
Version:	44906
Release:	2
Summary:	Include Scratch programs in LaTeX documents
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/scratchx
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/scratchx.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/scratchx.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package can be used to include every kind of Scratch
program in LaTeX documents. This may be particularly useful for
Math Teachers and IT specialists. The package depends on the
following other LaTeX packages: calc, fp, ifsym, multido, tikz,
xargs, and xstring.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/scratchx
%doc %{_texmfdistdir}/doc/latex/scratchx

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
