Summary:	console viewer for many graphics formats
Summary(de):	Konsolenbetrachter für viele Grafikformate
Summary(fr):	Visualiseur d'image en mode console, pour de nombreux formats graphiques
Summary(pl):	Konsolowa przegl±darka obrazków w ró¿nych formatach
Summary(tr):	Birçok resim formatýný görüntüleyebilen konsol aracý
Name:		zgv
Version:	5.0
Release:	1
License:	GPL
Group:		Applications/Graphics
Group(pl):	Aplikacje/Grafika
Source0:	ftp://metalab.unc.edu/pub/Linux/apps/graphics/viewers/svga/%{name}-%{version}.tar.gz
Patch0:		zgv-DESTDIR.patch
Patch1:		zgv-info.patch
BuildRequires:	svgalib-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Exclusivearch:	%{ix86} alpha

%description
Zgv is a picture viewer capable of displaying GIF files as defined by
CompuServe, with the exceptions listed in the RESTRICTIONS section. It
is also capable of displaying JPEG/JFIF files using the Independant
JPEG Group's JPEG software, PBM/PGM/PPM files as used by pbmplus and
netpbm, Microsoft Windows and OS/2 BMP files, Targa (TGA) files, and
the new PNG format.

%description -l de
zgv ist ein Bild-Viewer, der GIF-Dateien nach der
CompuServe-Definition anzeigen kann, abgesehen von den Ausnahmen im
Teil RESTRICTIONS. Ferner kann er JPEG/JFIF-Dateien unter Verwendung
der JPEG-Software der unabhängigen JPEG-Group, PBM/PGM/PPM-Dateien wie
sie pbmplus und netpbm benutzen, sowie Microsoft Windows und OS/2
BMB-Dateien, Targa (TGA) und das neue PNG-Format anzeigen.

%description -l fr
Zgv est un visualisateur de fichiers GIF tels que ceux qui sont
définis par CompuServe, avec les exceptions listées dans la section
RESTRICTIONS. Il peut aussi afficher les fichiers JPEG/JTIF utilisés
par le logiciel JPEG de l'Independant JPEG Group, les fichiers
PBM/PGM/PPM utilisés par pbmplus et netpbm, les fichiers BMP de
Microsoft Windows et OS/2, les fichiers Targa (TGA) et le nouveau
format PNG.

%description -l pl
Zgv potrafi wy¶wietlaæ obrazki w formacie CompuServe GIF (z wyj±tkami
opisanymi w rozdziale RESTRICTIONS), JPEG/JFIF, PBM/PGM/PPM, BMP (z
Microsoft Windows i OS/2), Targa (TGA) i PNG.

%description -l tr
Zgv, konsol ortamýndan CompuServe'in GIF formatý (RESTRICTIONS ile
belirtilenler dýþýnda), JPEG/JFIF, PGM/PBM/PPM, Bitmap (BMP), Targa
(TGA) ve yeni PNG formatlarýndaki resimleri görüntüleyebilmektedir.

%prep
%setup  -q
%patch0 -p1
%patch1 -p1

%build

%{__make} all OPTFLAGS="$RPM_OPT_FLAGS" \
	INCDIRS="-I%{_includedir}" \
	RGB_DB="%{_prefix}/X11R6/lib/X11/rgb.txt"

%{__make} info

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT \
	BINDIR=%{_bindir} \
	MANDIR=%{_mandir}/man1 \
	INFODIR=%{_infodir} \
	install

gzip -9nf TODO README README.fonts ChangeLog NEWS doc/sample.zgvrc \
	$RPM_BUILD_ROOT{%{_infodir}/%{name}*,%{_mandir}/man1/*}

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,README.fonts,ChangeLog,TODO,NEWS,doc/sample.zgvrc}.gz
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/*
%{_infodir}/*
