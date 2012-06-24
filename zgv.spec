#
# Conditional build:
%bcond_with	pcd	# with Kodak PhotoCD support
%bcond_without	svga	# don't build svgalib version
%bcond_without	sdl	# don't build SDL version
#
%ifnarch %{ix86} alpha
%define	_with_svga 0
%endif
Summary:	Console viewer for many graphics formats
Summary(de):	Konsolenbetrachter f�r viele Grafikformate
Summary(es):	Visualizador para muchos formatos de gr�ficos (consola)
Summary(fr):	Visualiseur d'image en mode console, pour de nombreux formats graphiques
Summary(pl):	Konsolowa przegl�darka obrazk�w w r�nych formatach
Summary(pt_BR):	Visualizador para muitos formatos de gr�ficos (console)
Summary(uk):	��������� �������� ��������� �������� ���Ʀ���� �����Ԧ�
Summary(tr):	Bir�ok resim format�n� g�r�nt�leyebilen konsol arac�
Summary(ru):	���������� ��������� ��������� ��������� ����������� ��������
Name:		zgv
Version:	5.7
Release:	2
License:	GPL
Group:		Applications/Graphics
Source0:	ftp://metalab.unc.edu/pub/Linux/apps/graphics/viewers/svga/%{name}-%{version}.tar.gz
# Source0-md5:	50f0127c250b6efe9c5f8850b96f3841
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-info.patch
Patch2:		%{name}-Dkey.patch
Patch3:		%{name}-gcc33.patch
Patch4:		%{name}-home_etc.patch
%{?with_sdl:BuildRequires:	SDL-devel}
BuildRequires:	gawk
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel >= 1.0.8
BuildRequires:	libtiff-devel
%{?with_svga:BuildRequires:	svgalib-devel}
BuildRequires:	texinfo
BuildRequires:	zlib-devel
%{?with_pcd:BuildRequires:	libpcd-devel}
Requires:	%{name}-common = %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%{!?with_sdl:%{!?with_svga:%{error: at least one version must be enabled} exit 1}}

%description
Zgv is a picture viewer capable of displaying GIF files as defined by
CompuServe, with the exceptions listed in the RESTRICTIONS section. It
is also capable of displaying JPEG/JFIF files using the Independant
JPEG Group's JPEG software, PBM/PGM/PPM files as used by pbmplus and
netpbm, Microsoft Windows and OS/2 BMP files, Targa (TGA) and TIFF
files, the new PNG format%{?_with_pcd: and PhotoCD}.

This package contains svgalib-based interface.

%description -l de
zgv ist ein Bild-Viewer, der GIF-Dateien nach der
CompuServe-Definition anzeigen kann, abgesehen von den Ausnahmen im
Teil RESTRICTIONS. Ferner kann er JPEG/JFIF-Dateien unter Verwendung
der JPEG-Software der unabh�ngigen JPEG-Group, PBM/PGM/PPM-Dateien wie
sie pbmplus und netpbm benutzen, sowie Microsoft Windows und OS/2
BMB-Dateien, Targa (TGA) und das neue PNG-Format anzeigen.

%description -l es
Zgv es un visualizador de im�genes capaz de ense�ar archivos tipo
"GIF" como las definidas por la CompuServe. Tambi�n es capaz de
ense�ar archivos JPEG/JFIF usando "Independant JPEG Group JPEG
software", archivos PBM/PGM/PPM como los usados por la pbmplus y
netpbm, archivos Microsoft Windows y OS/2 BMP, archivos Targa (TGA), y
el nuevo formato PNG.

%description -l fr
Zgv est un visualisateur de fichiers GIF tels que ceux qui sont
d�finis par CompuServe, avec les exceptions list�es dans la section
RESTRICTIONS. Il peut aussi afficher les fichiers JPEG/JTIF utilis�s
par le logiciel JPEG de l'Independant JPEG Group, les fichiers
PBM/PGM/PPM utilis�s par pbmplus et netpbm, les fichiers BMP de
Microsoft Windows et OS/2, les fichiers Targa (TGA) et le nouveau
format PNG.

%description -l pl
Zgv potrafi wy�wietla� obrazki w formacie CompuServe GIF (z wyj�tkami
opisanymi w rozdziale RESTRICTIONS), JPEG/JFIF, PBM/PGM/PPM, BMP (z
Microsoft Windows i OS/2), Targa (TGA), TIFF, PNG%{?_with_pcd: i PhotoCD}.

Ten pakiet zawiera interfejs korzystajacy z biblioteki svgalib.

%description -l pt_BR
Zgv � um visualizador de imagens capaz de mostrar arquivos tipo "GIF"
como as definidas pela CompuServe. Ele tamb�m � capaz de mostrar
arquivos JPEG/JFIF usando o "Independent JPEG Group JPEG software",
arquivos PBM/PGM/PPM como os usados pela pbmplus e netpbm, arquivos
Microsoft Windows e OS/2 BMP, arquivos Targa (TGA), e o novo formato
PNG.

%description -l ru
Zgv - ��� ��������� ��� ��������� �����������, ������� ������������
����� ������ � �������� GIF, JPEG/JFIF, PNG, PBM/PGM/PPM, BMP, TGA,
PCX � MRF �� VGA � SVGA ��������. Zgv ����� ����� ����������
����-����� ����������� (thumbnails). Zgv ������������ �� svgalib,
������� ��� ������������� zgv ��� ���������� �� ����������.

%description -l tr
Zgv, konsol ortam�ndan CompuServe'in GIF format� (RESTRICTIONS ile
belirtilenler d���nda), JPEG/JFIF, PGM/PBM/PPM, Bitmap (BMP), Targa
(TGA) ve yeni PNG formatlar�ndaki resimleri g�r�nt�leyebilmektedir.

%description -l uk
Zgv - �� �������� ��� ��������� ���������, ��� Ц�����դ ����� ���̦�
� �������� GIF, JPEG/JFIF, PNG, PBM/PGM/PPM, BMP, TGA, PCX � MRF ��
VGA �� SVGA ��������. Zgv ���� ����� ���������� ͦΦ-��Ц� ���������
(thumbnails). Zgv ���դ���� �� svgalib, ���� ��� ������������ zgv ���
����Ȧ��� �� ����������,

%package common
Summary:	Common files for both ZGV frontends
Summary(pl):	Pakiet wsp�lny dla obu interfejs�w ZGV
Group:		Applications/Graphics
Requires:	/usr/X11R6/lib/X11/rgb.txt

%description common
Common files for both ZGV frontends.

%description common -l pl
Pakiet wsp�lny dla obu interfejs�w ZGV.

%package sdl
Summary:	SDL viewer for many graphics formats
Summary(pl):	Oparta na SDL przegl�darka obrazk�w w r�nych formatach
Group:		Applications/Graphics
Requires:	%{name}-common = %{version}

%description sdl
Zgv is a picture viewer capable of displaying GIF files as defined by
CompuServe, with the exceptions listed in the RESTRICTIONS section. It
is also capable of displaying JPEG/JFIF files using the Independant
JPEG Group's JPEG software, PBM/PGM/PPM files as used by pbmplus and
netpbm, Microsoft Windows and OS/2 BMP files, Targa (TGA) and TIFF
files, the new PNG format%{?_with_pcd: and PhotoCD}.

This package contains SDL-based interfeace.

%description sdl -l pl
Zgv potrafi wy�wietla� obrazki w formacie CompuServe GIF (z wyj�tkami
opisanymi w rozdziale RESTRICTIONS), JPEG/JFIF, PBM/PGM/PPM, BMP (z
Microsoft Windows i OS/2), Targa (TGA), TIFF, PNG%{?_with_pcd: i PhotoCD}.

Ten pakiet zawiera interfejs korzystajacy z biblioteki SDL.

%prep
%setup  -q
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
	RGB_DB="/usr/X11R6/lib/X11/rgb.txt"

%{?with_sdl:mv -f src/zgv zgv-svga}
%{?with_sdl:%{__make} clean}
%endif

%if %{with sdl}
%{__make} all \
	OPTFLAGS="%{rpmcflags}" \
	BACKEND=SDL \
	RGB_DB="/usr/X11R6/lib/X11/rgb.txt"
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

install doc/sample.zgvrc $RPM_BUILD_ROOT%{_sysconfdir}/zgv.conf

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

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
