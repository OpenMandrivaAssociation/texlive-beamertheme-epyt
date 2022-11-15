Name:		texlive-beamertheme-epyt
Version:	41404
Release:	1
Summary:	A simple and clean theme for LaTeX beamer class
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/beamertheme-epyt
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beamertheme-epyt.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beamertheme-epyt.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides a simple but nice theme for Beamer, with
the following features: simple structure: with page numbers at
footer, no head bar and side bar simple templates: displaying
theorems with traditional inline style simple colors: using
only several foreground and background colors

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/beamertheme-epyt
%doc %{_texmfdistdir}/doc/latex/beamertheme-epyt

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
