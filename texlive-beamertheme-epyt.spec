%global tl_name beamertheme-epyt
%global tl_revision 41404

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	A simple and clean theme for LaTeX beamer class
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/beamer-contrib/themes/beamertheme-epyt
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/beamertheme-epyt.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/beamertheme-epyt.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides a simple but nice theme for Beamer, with the
following features: simple structure: with page numbers at footer, no
head bar and side bar simple templates: displaying theorems with
traditional inline style simple colors: using only several foreground
and background colors

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/beamertheme-epyt
%dir %{_datadir}/texmf-dist/tex/latex/beamertheme-epyt
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-epyt/README
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-epyt/epyt-demo-cn.pdf
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-epyt/epyt-demo-cn.tex
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-epyt/epyt-demo.pdf
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-epyt/epyt-demo.tex
%{_datadir}/texmf-dist/tex/latex/beamertheme-epyt/beamerthemeepyt.sty
