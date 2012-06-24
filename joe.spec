Summary:	Easy to use editor
Summary(de):	einfach handzuhabender Editor
Summary(fr):	�diteur facile � utiliser
Summary(pl):	�atwy w u�yciu edytor tekstowy
Summary(tr):	Kolay kullan�ml� metin d�zenleyici
Name:		joe
Version:	2.8
Release:	20
Copyright:	GPL
Group:		Applications/Editors
Group(pl):	Aplikacje/Edytory
Source:		ftp://ftp.std.com/src/editors/%{name}%{version}.tar.Z
Patch0:		joe-config.patch
Patch1:		joe-time.patch
Patch2:		joe-axphack.patch
Patch3:		joe-make.patch
Patch4:		joe-asis.patch
Patch5:		joe-man.patch
Patch6:		joe-mips.patch
Patch7:		joe-port.patch
Patch8:		joe-kbdfix.patch
Patch9:		joe-locale.patch
BuildPrereq:	ncurses-devel
Buildroot:	/tmp/%{name}-%{version}-root

%description
Joe is a friendly and easy to use editor.  It has a nice interface and would 
be a good choice for a novice needing a text editor. It uses the same WordStar
keybindings which are also used by Borland's development enbironment.

%description -l de
Joe ist ein bedienerfreundlicher, einfacher Editor mit attraktiver Oberfl�che. 
Eine gute Wahl f�r Neueinsteiger, die einen Texteditor brauchen, benutzt er
dieselben WordStar-Keybindings, die auch von Borlands Enwicklungsumgebung
verwendet werden.

%description -l fr
Joe est un �diteur de texte simple � utiliser. il � une interface agr�able
et constitue un bon choix novice ayant besoin d'un �diteur de texte. Il
utilise les m�mes combinaisons de touches que WordStar, qui sont aussi
utilis�es par les environnements de d�veloppement Borland.

%description -l pl
Joe jest �atwym i przyjemnym w u�yciu edytorem, ma �adny interfejs i mo�e by�
dobrym wyborem dla pocz�tkuj�cych u�ytkownik�w Linuxa. Joe u�ywa tej samej
kombinacji klawiszy co WordStar i oprogramowae Borland'a.

%description -l tr
Joe, k���k ve kullan�m� kolay bir metin d�zenleyicisidir. Borland firmas�n�n
geli�tirme ortam�na al��k�n olanlar ayn� k�sayol tu�lar�n� kullanmaktan
memnun olacaklard�r. Basitli�i nedeni ile ba�layanlar i�in en cok tavsiye
edilen metin d�zenleyicisidir.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1

%ifarch axp
%patch2 -p1
%endif

%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p0

%build
make	WHEREJOE=%{_bindir} \
	WHERERC=/etc/joe
	
%install
rm -rf $RPM_BUILD_ROOT
make install \
	WHEREJOE=$RPM_BUILD_ROOT%{_bindir} \
	WHERERC=$RPM_BUILD_ROOT/etc/joe \
	WHEREMAN=$RPM_BUILD_ROOT%{_mandir}/man1

echo ".so joe" > $RPM_BUILD_ROOT%{_mandir}/man1/jstar.1
echo ".so joe" > $RPM_BUILD_ROOT%{_mandir}/man1/jmacs.1
echo ".so joe" > $RPM_BUILD_ROOT%{_mandir}/man1/rjoe.1
echo ".so joe" > $RPM_BUILD_ROOT%{_mandir}/man1/jpico.1

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%dir /etc/joe
%config /etc/joe/*
%{_mandir}/man1/*

%changelog
* Sat Apr 24 1999 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [2.8-20]
- added joe-locale.patch (from rawhide),
- recompiles on new rpm.

* Thu Mar  4 1999 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [2.8-19]
- added joe-kbdfix.patch with fix End key handling.

* Mon Feb 22 1999 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [2.8-18]
- removed man group from man pages.

* Wed Feb 17 1999 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [2.8-17]
- simplification in %files,
- added man, mips and potr patches,
- added man pages for jstar, jmacs, rjoe and jpico as *roff include to
  joe(1),
- back to libncurses,
- added "Requires: ncurses >= 4.2-12" for prevent installing joe
  with proper version ncurses.

* Thu Aug 27 1998 Wojtek �lusarczyk <wojtek@shadow.eu.org>
  [2.8-14]
- added patch adopted from Debian sources,
- added pl translation.

* Mon Jul 20 1998 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
- added %attr macros in %filles (allow build joe from non-root account),
- added -q %setup parameter,
- config files moved to /etc,
- joe is now linked with libslang.

* Fri May 08 1998 Cristian Gafton <gafton@redhat.com>
- enable -asis in the config files so international keyboards will be better
  supported
  
* Fri May 01 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Fri May 01 1998 Cristian Gafton <gafton@redhat.com>
- /usr/lib/joe/* are config files 

* Thu Apr 09 1998 Cristian Gafton <gafton@redhat.com>
- manhattan build 

* Thu Dec 11 1997 Cristian Gafton <gafton@redhat.com>
- fixed termcap problems for terms other than 80x25
- added support for buildroot and BuildRoot

* Mon Jul 21 1997 Erik Troan <ewt@redhat.com>
- built against glibcc
