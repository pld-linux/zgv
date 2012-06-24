#
# _with_pcd - with Kodak PhotoCD support
Summary:	console viewer for many graphics formats
Summary(de):	Konsolenbetrachter f�r viele Grafikformate
Summary(es):	Visualizador para muchos formatos de gr�ficos (consola)
Summary(fr):	Visualiseur d'image en mode console, pour de nombreux formats graphiques
Summary(pl):	Konsolowa przegl�darka obrazk�w w r�nych formatach
Summary(pt_BR):	Visualizador para muitos formatos de gr�ficos (console)
Summary(uk):	��������� �������� ��������� �������� ���Ʀ���� �����Ԧ�
Summary(tr):	Bir�ok resim format�n� g�r�nt�leyebilen konsol arac�
Summary(ru):	���������� ��������� ��������� ��������� ����������� ��������
Name:		zgv
Version:	5.6
Release:	1
License:	GPL
Group:		Applications/Graphics
Source0:	ftp://metalab.unc.edu/pub/Linux/apps/graphics/viewers/svga/%{name}-%{version}.tar.gz
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-info.patch
Patch2:		%{name}-Dkey.patch
BuildRequires:	gawk
BuildRequires:	libjpeg-devel
BuildRequires:	libpng >= 1.0.8
BuildRequires:	libtiff-devel
BuildRequires:	svgalib-devel
BuildRequires:	texinfo
BuildRequires:	zlib-devel
%{?_with_pcd:BuildRequires: libpcd-devel}
Requires:	/usr/X11R6/lib/X11/rgb.txt
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
ExclusiveArch:	%{ix86} alpha

%description
Zgv is a picture viewer capable of displaying GIF files as defined by
CompuServe, with the exceptions listed in the RESTRICTIONS section. It
is also capable of displaying JPEG/JFIF files using the Independant
JPEG Group's JPEG software, PBM/PGM/PPM files as used by pbmplus and
netpbm, Microsoft Windows and OS/2 BMP files, Targa (TGA) and TIFF
files, the new PNG format%{?_with_pcd: and PhotoCD}.

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

%prep
%setup  -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%if %{?_with_pcd:1}%{!?_with_pcd:0}
sed -e 's@#\(PCDDEF=.*\)@\1@' config.mk > config.mk.new
mv -f config.mk.new config.mk
%endif

%build
%{__make} all OPTFLAGS="%{rpmcflags} `pkg-config --cflags libpng12 2>/dev/null`" \
	RGB_DB="%{_prefix}/X11R6/lib/X11/rgb.txt"

%{__make} info

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	BINDIR=%{_bindir} \
	MANDIR=%{_mandir}/man1 \
	INFODIR=%{_infodir}

install doc/sample.zgvrc $RPM_BUILD_ROOT%{_sysconfdir}/zgv.conf

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README* TODO
%config(noreplace,missingok) %verify(not md5 mtime size) %{_sysconfdir}/zgv.conf
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/*
%{_infodir}/*
