Summary:	Easy to use editor
Summary(de):	einfach handzuhabender Editor
Summary(fr):	�diteur facile � utiliser
Summary(pl):	�atwy w u�yciu edytor tekstowy
Summary(tr):	Kolay kullan�ml� metin d�zenleyici
Name:		joe
Version:	2.8
Release:	28
License:	GPL
Group:		Applications/Editors
Group(pt):	X11/Aplica��es/Editores
Group(pl):	Aplikacje/Edytory
Source0:	ftp://ftp.std.com/src/editors/%{name}%{version}.tar.Z
Source1:	joe.png
Source2:	joe.desktop
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
Patch10:	joe-deadjoe.patch
Patch11:	joe-security.patch
Patch12:	joe-resize.patch
Patch13:	joe-segv.patch
Icon:		joe.xpm
BuildRequires:	ncurses-devel >= 5.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Joe is a friendly and easy to use editor. It has a nice interface and
would be a good choice for a novice needing a text editor. It uses the
same WordStar keybindings which are also used by Borland's development
enbironment.

%description -l de
Joe ist ein bedienerfreundlicher, einfacher Editor mit attraktiver
Oberfl�che. Eine gute Wahl f�r Neueinsteiger, die einen Texteditor
brauchen, benutzt er dieselben WordStar-Keybindings, die auch von
Borlands Enwicklungsumgebung verwendet werden.

%description -l fr
Joe est un �diteur de texte simple � utiliser. il � une interface
agr�able et constitue un bon choix novice ayant besoin d'un �diteur de
texte. Il utilise les m�mes combinaisons de touches que WordStar, qui
sont aussi utilis�es par les environnements de d�veloppement Borland.

%description -l pl
Joe jest �atwym i przyjemnym w u�yciu edytorem, ma �adny interfejs i
mo�e by� dobrym wyborem dla pocz�tkuj�cych u�ytkownik�w Linuxa. Joe
u�ywa tej samej kombinacji klawiszy co WordStar i oprogramowae
Borland'a.

%description -l tr
Joe, k���k ve kullan�m� kolay bir metin d�zenleyicisidir. Borland
firmas�n�n geli�tirme ortam�na al��k�n olanlar ayn� k�sayol tu�lar�n�
kullanmaktan memnun olacaklard�r. Basitli�i nedeni ile ba�layanlar
i�in en cok tavsiye edilen metin d�zenleyicisidir.

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
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1

%build
make	WHEREJOE=%{_bindir} \
WHERERC=%{_sysconfdir}/joe
	
%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Editors,%{_prefix}/X11R6/share/pixmaps}

%{__make} install \
	WHEREJOE=$RPM_BUILD_ROOT%{_bindir} \
	WHERERC=$RPM_BUILD_ROOT%{_sysconfdir}/joe \
	WHEREMAN=$RPM_BUILD_ROOT%{_mandir}/man1

echo ".so joe" > $RPM_BUILD_ROOT%{_mandir}/man1/jstar.1
echo ".so joe" > $RPM_BUILD_ROOT%{_mandir}/man1/jmacs.1
echo ".so joe" > $RPM_BUILD_ROOT%{_mandir}/man1/rjoe.1
echo ".so joe" > $RPM_BUILD_ROOT%{_mandir}/man1/jpico.1

install %{SOURCE1} $RPM_BUILD_ROOT%{_prefix}/X11R6/share/pixmaps
install %{SOURCE2} $RPM_BUILD_ROOT%{_applnkdir}/Editors

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%dir %{_sysconfdir}/joe
%config %{_sysconfdir}/joe/*
%{_mandir}/man1/*
%{_applnkdir}/Editors/*
%{_prefix}/X11R6/share/pixmaps/*
