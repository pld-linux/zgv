Summary:	console viewer for many graphics formats
Summary(de):	Konsolenbetrachter für viele Grafikformate
Summary(fr):	Visualiseur d'image en mode console, pour de nombreux formats graphiques.
Summary(pl):	Konsolowa przegl±darka obrazków w ró¿nych formatach
Summary(tr):	Birçok resim formatýný görüntüleyebilen konsol aracý
Name:		zgv
Version:	3.2
Release:	3
Copyright:	GPL
Group:		Applications/Graphics
Group(pl):	Aplikacje/Grafika
Source:		ftp://sunsite.unc.edu/pub/Linux/apps/graphics/viewers/svga/%{name}-%{version}.tar.gz
Patch0:		zgv-makefile.patch
Patch1:		zgv-info.patch
BuildPrereq:	svgalib-devel
BuildPrereq:	libjpeg-devel
BuildPrereq:	libpng-devel
BuildPrereq:	zlib-devel
BuildRoot:	/tmp/%{name}-%{version}-root
Exclusivearch:	%{ix86} alpha

%description
Zgv is a picture viewer capable of displaying GIF files as defined by
CompuServe, with the exceptions listed in the RESTRICTIONS section. It
is also capable of displaying JPEG/JFIF files using the Independant
JPEG Group's JPEG software, PBM/PGM/PPM files as used by pbmplus and
netpbm, Microsoft Windows and OS/2 BMP files, Targa (TGA) files, and
the new PNG format.

%description -l de
zgv ist ein Bild-Viewer, der GIF-Dateien nach der CompuServe-Definition 
anzeigen kann, abgesehen von den Ausnahmen im Teil RESTRICTIONS. Ferner 
kann er JPEG/JFIF-Dateien unter Verwendung der JPEG-Software der 
unabhängigen JPEG-Group, PBM/PGM/PPM-Dateien wie sie pbmplus und netpbm 
benutzen, sowie Microsoft Windows und OS/2 BMB-Dateien, Targa (TGA) und 
das neue PNG-Format anzeigen.

%description -l fr
Zgv est un visualisateur de fichiers GIF tels que ceux qui sont définis
par CompuServe, avec les exceptions listées dans la section RESTRICTIONS.
Il peut aussi afficher les fichiers JPEG/JTIF utilisés par le logiciel
JPEG de l'Independant JPEG Group, les fichiers PBM/PGM/PPM utilisés par
pbmplus et netpbm, les fichiers BMP de Microsoft Windows et OS/2,
les fichiers Targa (TGA) et le nouveau format PNG.

%description -l pl
Zgv potrafi wy¶wietlaæ obrazki w formacie CompuServe GIF (z wyj±tkami
opisanymi w rozdziale RESTRICTIONS), JPEG/JFIF, PBM/PGM/PPM, BMP
(z Microsoft Windows i OS/2), Targa (TGA) i PNG.

%description -l tr
Zgv, konsol ortamýndan CompuServe'in GIF formatý (RESTRICTIONS ile
belirtilenler dýþýnda), JPEG/JFIF, PGM/PBM/PPM, Bitmap (BMP), Targa (TGA) ve
yeni PNG formatlarýndaki resimleri görüntüleyebilmektedir.

%prep
%setup  -q
%patch0 -p1
%patch1 -p1

%build

make all OPTFLAGS="$RPM_OPT_FLAGS" \
	INCDIRS="-I%{_includedir}" \
	RGB_DB="/usr/X11R6/lib/X11/rgb.txt"

make info

%install
rm -rf $RPM_BUILD_ROOT

make PREFIX="$RPM_BUILD_ROOT/usr" install

gzip -9nf TODO README README.fonts ChangeLog NEWS doc/sample.zgvrc \
	$RPM_BUILD_ROOT/usr/{share/info/zgv*,share/man/man1/*}

%post
/sbin/install-info %{_infodir}/zgv.gz /etc/info-dir

%preun
if [ "$1" = "0" ]; then
        /sbin/install-info --delete %{_infodir}/zgv.gz /etc/info-dir
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,README.fonts,ChangeLog,TODO,NEWS,doc/sample.zgvrc}.gz

%attr(4511,root,root) %{_bindir}/zgv

%{_mandir}/man1/zgv.1.*
%{_infodir}/zgv*

%changelog
* Mon May 10 1999 Piotr Czerwiñski <pius@pld.org.pl>
  [3.2-3]
- updated zgv-makefile.patch,
- package is now FHS 2.0 compliant.

* Wed Apr 21 1999 Piotr Czerwiñski <pius@pld.org.pl>
  [3.2-2]
- recompiled on rpm3,
- cosmetic changes.

* Sat Mar 27 1999 Piotr Czerwiñski <pius@pld.org.pl>
  [3.2-1]
- updated to 3.2,
- removed zgv-3.0-redhat.patch and zgv2.7-glibc.patch,
- added zgv-makefile.patch (fixed passing $RPM_OPT_FLAGS, changed install
  procedure to allow building from non-root account),
- rewritten %build,
- simplifications in %install,
- added info files,
- added %post and %preun.

* Wed Mar 24 1999 Piotr Czerwiñski <pius@pld.org.pl>
- changed BuildRoot to /tmp/%%{name}-%%{version}-root,
- added Group(pl),
- added %deffatr description in %files,
- added documentation,
- added gzipping documentation and man pages,
- removed man group from man pages,
- cosmetic changes.

* Thu Sep 24 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [3.0-6]
- added aplha to Exclusivearch list.

* Thu Sep 24 1998 Marcin 'Qrczak' Kowalczyk <qrczak@knm.org.pl>
- added BuildRoot,
- added full %attr description in %files,
- allow building from non-root account (set suid root only in %attr),
- added pl translation.

* Tue Aug  4 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Wed Jun 10 1998 Prospector System <bugs@redhat.com>
- translations modified for de

* Fri Apr 24 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Mon Apr 20 1998 Erik Troan <ewt@redhat.com>
- updated to version 3.0

* Tue Oct 21 1997 Michael Fulbright <msf@redhat.com>
- updated spec file and upgraded to version 2.8

* Wed Oct 15 1997 Erik Troan <ewt@redhat.com>
- build against new libpng

* Fri Aug 22 1997 Erik Troan <ewt@redhat.com>
- built against glibc
