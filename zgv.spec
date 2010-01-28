#
# Conditional build:
%bcond_with	pcd	# with Kodak PhotoCD support
%bcond_without	svga	# don't build svgalib version
%bcond_without	sdl	# don't build SDL version
#
Summary:	Console viewer for many graphics formats
Summary(de.UTF-8):	Konsolenbetrachter für viele Grafikformate
Summary(es.UTF-8):	Visualizador para muchos formatos de gráficos (consola)
Summary(fr.UTF-8):	Visualiseur d'image en mode console, pour de nombreux formats graphiques
Summary(pl.UTF-8):	Konsolowa przeglądarka obrazków w różnych formatach
Summary(pt_BR.UTF-8):	Visualizador para muitos formatos de gráficos (console)
Summary(uk.UTF-8):	Консольна програма перегляду багатьох графічних форматів
Summary(tr.UTF-8):	Birçok resim formatını görüntüleyebilen konsol aracı
Summary(ru.UTF-8):	Консольная программа просмотра множества графических форматов
Name:		zgv
Version:	5.9
Release:	6
License:	GPL
Group:		Applications/Graphics
Source0:	ftp://metalab.unc.edu/pub/Linux/apps/graphics/viewers/svga/%{name}-%{version}.tar.gz
# Source0-md5:	d65a434ddeb612f0c488177f873afad2
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-info.patch
Patch2:		%{name}-Dkey.patch
Patch3:		%{name}-home_etc.patch
Patch4:		%{name}-gcc.patch
%{?with_sdl:BuildRequires:	SDL-devel}
BuildRequires:	gawk
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel >= 1.0.8
BuildRequires:	libtiff-devel
%{?with_svga:BuildRequires:	svgalib-devel}
BuildRequires:	texinfo
BuildRequires:	zlib-devel
%{?with_pcd:BuildRequires:	libpcd-devel}
Requires:	%{name}-common = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%{!?with_sdl:%{!?with_svga:%{error: at least one version must be enabled} exit 1}}

%description
Zgv is a picture viewer capable of displaying GIF files as defined by
CompuServe, with the exceptions listed in the RESTRICTIONS section. It
is also capable of displaying JPEG/JFIF files using the Independant
JPEG Group's JPEG software, PBM/PGM/PPM files as used by pbmplus and
netpbm, Microsoft Windows and OS/2 BMP files, Targa (TGA) and TIFF
files, the new PNG format%{?with_pcd: and PhotoCD}.

This package contains svgalib-based interface.

%description -l de.UTF-8
zgv ist ein Bild-Viewer, der GIF-Dateien nach der
CompuServe-Definition anzeigen kann, abgesehen von den Ausnahmen im
Teil RESTRICTIONS. Ferner kann er JPEG/JFIF-Dateien unter Verwendung
der JPEG-Software der unabhängigen JPEG-Group, PBM/PGM/PPM-Dateien wie
sie pbmplus und netpbm benutzen, sowie Microsoft Windows und OS/2
BMB-Dateien, Targa (TGA) und das neue PNG-Format anzeigen.

%description -l es.UTF-8
Zgv es un visualizador de imágenes capaz de enseñar archivos tipo
"GIF" como las definidas por la CompuServe. También es capaz de
enseñar archivos JPEG/JFIF usando "Independant JPEG Group JPEG
software", archivos PBM/PGM/PPM como los usados por la pbmplus y
netpbm, archivos Microsoft Windows y OS/2 BMP, archivos Targa (TGA), y
el nuevo formato PNG.

%description -l fr.UTF-8
Zgv est un visualisateur de fichiers GIF tels que ceux qui sont
définis par CompuServe, avec les exceptions listées dans la section
RESTRICTIONS. Il peut aussi afficher les fichiers JPEG/JTIF utilisés
par le logiciel JPEG de l'Independant JPEG Group, les fichiers
PBM/PGM/PPM utilisés par pbmplus et netpbm, les fichiers BMP de
Microsoft Windows et OS/2, les fichiers Targa (TGA) et le nouveau
format PNG.

%description -l pl.UTF-8
Zgv potrafi wyświetlać obrazki w formacie CompuServe GIF (z wyjątkami
opisanymi w rozdziale RESTRICTIONS), JPEG/JFIF, PBM/PGM/PPM, BMP (z
Microsoft Windows i OS/2), Targa (TGA), TIFF, PNG%{?with_pcd: i PhotoCD}.

Ten pakiet zawiera interfejs korzystajacy z biblioteki svgalib.

%description -l pt_BR.UTF-8
Zgv é um visualizador de imagens capaz de mostrar arquivos tipo "GIF"
como as definidas pela CompuServe. Ele também é capaz de mostrar
arquivos JPEG/JFIF usando o "Independent JPEG Group JPEG software",
arquivos PBM/PGM/PPM como os usados pela pbmplus e netpbm, arquivos
Microsoft Windows e OS/2 BMP, arquivos Targa (TGA), e o novo formato
PNG.

%description -l ru.UTF-8
Zgv - это программа для просмотра изображений, которая поддерживает
показ файлов в форматах GIF, JPEG/JFIF, PNG, PBM/PGM/PPM, BMP, TGA,
PCX и MRF на VGA и SVGA дисплеях. Zgv может также показывать
мини-копии изображений (thumbnails). Zgv основывается на svgalib,
поэтому для использования zgv вам необходимо ее установить.

%description -l tr.UTF-8
Zgv, konsol ortamından CompuServe'in GIF formatı (RESTRICTIONS ile
belirtilenler dışında), JPEG/JFIF, PGM/PBM/PPM, Bitmap (BMP), Targa
(TGA) ve yeni PNG formatlarındaki resimleri görüntüleyebilmektedir.

%description -l uk.UTF-8
Zgv - це програма для перегляду зображень, яка підтримує показ файлів
в форматах GIF, JPEG/JFIF, PNG, PBM/PGM/PPM, BMP, TGA, PCX і MRF на
VGA та SVGA дисплеях. Zgv може також показувати міні-копії зображень
(thumbnails). Zgv базується на svgalib, тому для використання zgv вам
необхідно її встановити,

%package common
Summary:	Common files for both ZGV frontends
Summary(pl.UTF-8):	Pakiet wspólny dla obu interfejsów ZGV
Group:		Applications/Graphics
Requires:	/usr/share/X11/rgb.txt

%description common
Common files for both ZGV frontends.

%description common -l pl.UTF-8
Pakiet wspólny dla obu interfejsów ZGV.

%package sdl
Summary:	SDL viewer for many graphics formats
Summary(pl.UTF-8):	Oparta na SDL przeglądarka obrazków w różnych formatach
Group:		Applications/Graphics
Requires:	%{name}-common = %{version}-%{release}

%description sdl
Zgv is a picture viewer capable of displaying GIF files as defined by
CompuServe, with the exceptions listed in the RESTRICTIONS section. It
is also capable of displaying JPEG/JFIF files using the Independant
JPEG Group's JPEG software, PBM/PGM/PPM files as used by pbmplus and
netpbm, Microsoft Windows and OS/2 BMP files, Targa (TGA) and TIFF
files, the new PNG format%{?with_pcd: and PhotoCD}.

This package contains SDL-based interfeace.

%description sdl -l pl.UTF-8
Zgv potrafi wyświetlać obrazki w formacie CompuServe GIF (z wyjątkami
opisanymi w rozdziale RESTRICTIONS), JPEG/JFIF, PBM/PGM/PPM, BMP (z
Microsoft Windows i OS/2), Targa (TGA), TIFF, PNG%{?with_pcd: i PhotoCD}.

Ten pakiet zawiera interfejs korzystajacy z biblioteki SDL.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%if %{with pcd}
sed -e 's@#\(PCDDEF=.*\)@\1@' config.mk > config.mk.new
mv -f config.mk.new config.mk
%endif

%build
%if %{with svga}
%{__make} all \
	OPTFLAGS="%{rpmcflags}" \
	RGB_DB="/usr/share/X11/rgb.txt" \
	RCFILE="%{_sysconfdir}/zgv.conf" \
	CC="%{__cc}"

%{?with_sdl:mv -f src/zgv zgv-svga}
%{?with_sdl:%{__make} clean}
%endif

%if %{with sdl}
%{__make} all \
	OPTFLAGS="%{rpmcflags}" \
	BACKEND=SDL \
	RGB_DB="/usr/share/X11/rgb.txt" \
	RCFILE="%{_sysconfdir}/zgv.conf" \
	CC="%{__cc}"
%endif

%{__make} info

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	BINDIR=%{_bindir} \
	MANDIR=%{_mandir}/man1 \
	INFODIR=%{_infodir} \
	%{?with_sdl:BACKEND=SDL}

%{?with_svga:%{?with_sdl:install zgv-svga $RPM_BUILD_ROOT%{_bindir}/zgv}}
%{?with_sdl:echo '.so zgv.1' > $RPM_BUILD_ROOT%{_mandir}/man1/zgv-sdl.1}

sed -e "s@/usr/local/etc@%{_sysconfdir}@g" doc/sample.zgvrc >$RPM_BUILD_ROOT%{_sysconfdir}/zgv.conf

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%if %{with svga}
%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/zgv
%endif

%files common
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README* TODO
%config(noreplace,missingok) %verify(not md5 mtime size) %{_sysconfdir}/zgv.conf
%{_mandir}/man1/zgv.1*
%{_infodir}/*.info*

%if %{with sdl}
%files sdl
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/zgv-sdl
%{_mandir}/man1/zgv-sdl.1*
%endif
