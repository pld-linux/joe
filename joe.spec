Summary:     Easy to use editor
Name:        joe
Version:     2.8
Release:     14
Copyright:   GPL
Group:       Applications/Editors
Group(pl):   Aplikacje/Edytory
Source:      ftp://ftp.std.com/src/editors/%{name}%{version}.tar.Z
Patch0:      joe2.8-config.patch
Patch1:      joe2.8-time.patch
Patch2:      joe2.8-axphack.patch
Patch3:      joe2.8-make.patch
Patch4:      joe-2.8-asis.patch
Patch5:      joe-2.8.patch
Buildroot:   /tmp/buildroot-%{name}-%{version}
Summary(de): einfach handzuhabender Editor
Summary(fr): éditeur facile à utiliser
Summary(pl): £atwy w u¿yciu edytor tekstowy
Summary(tr): Kolay kullanýmlý metin düzenleyici

%description
Joe is a friendly and easy to use editor.  It has a nice interface and would 
be a good choice for a novice needing a text editor. It uses the same WordStar
keybindings which are also used by Borland's development enbironment.

%description -l de
Joe ist ein bedienerfreundlicher, einfacher Editor mit attraktiver Oberfläche. 
Eine gute Wahl für Neueinsteiger, die einen Texteditor brauchen, benutzt er
dieselben WordStar-Keybindings, die auch von Borlands Enwicklungsumgebung
verwendet werden.

%description -l fr
Joe est un éditeur de texte simple à utiliser. il à une interface agréable
et constitue un bon choix novice ayant besoin d'un éditeur de texte. Il
utilise les mêmes combinaisons de touches que WordStar, qui sont aussi
utilisées par les environnements de développement Borland.

%description -l pl
Joe jest ³atwym i przyjemnym w u¿yciu edytorem, ma ³adny interfejs i mo¿e byæ
dobrym wyborem dla pocz±tkuj±cych u¿ytkowników Linuxa. Joe u¿ywa tej samej
kombinacji klawiszy co WordStar i oprogramowae Borland'a.

%description -l tr
Joe, küçük ve kullanýmý kolay bir metin düzenleyicisidir. Borland firmasýnýn
geliþtirme ortamýna alýþkýn olanlar ayný kýsayol tuþlarýný kullanmaktan
memnun olacaklardýr. Basitliði nedeni ile baþlayanlar için en cok tavsiye
edilen metin düzenleyicisidir.

%prep
%setup -q -n %{name}
%patch0 -p1 -b .config
%patch1 -p1 -b .time

%ifarch axp
%patch2 -p1 -b .axp
%endif

%patch3 -p1 -b .make
%patch4 -p1 -b .asis
%patch5 -p1

%build
make	CFLAGS="$RPM_OPT_FLAGS" \
	EXTRALIBS=-lncurses \
	WHEREJOE=/usr/bin \
	WHERERC=/etc/joe \
	
%install
rm -rf $RPM_BUILD_ROOT
make install \
	WHEREJOE=$RPM_BUILD_ROOT/usr/bin \
	WHERERC=$RPM_BUILD_ROOT/etc/joe \
	WHEREMAN=$RPM_BUILD_ROOT/usr/man/man1

gzip -9nf $RPM_BUILD_ROOT/usr/man/man*/*

%files
%attr(755, root, root) /usr/bin/*
%attr(755, root, root) %dir /etc/joe
%attr(644, root, root) %config /etc/joe/*
%attr(644, root,  man) /usr/man/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Thu Aug 27 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [2.8.14]
- added patch adopted from Debian sources,
- added pl translation.

* Mon Jul 20 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
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
- built against glibc
