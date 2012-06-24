Summary:	Easy to use editor
Summary(de):	einfach handzuhabender Editor
Summary(fr):	�diteur facile � utiliser
Summary(pl):	�atwy w u�yciu edytor tekstowy
Summary(tr):	Kolay kullan�ml� metin d�zenleyici
Name:		joe
Version:	2.9.6
Release:	2
License:	GPL
Group:		Applications/Editors
Group(de):	Applikationen/Editors
Group(pl):	Aplikacje/Edytory
Group(pt):	Aplica��es/Editores
Source0:	http://prdownloads.sourceforge.net/joe-editor/%{name}-%{version}.tgz
Source1:	%{name}.png
Source2:	%{name}.desktop
Patch0:		%{name}-Makefile_fix.patch
Icon:		joe.xpm
URL:		http://sourceforge.net/projects/joe-editor/
BuildRequires:	ncurses-devel >= 5.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/joe

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
%setup -q
%patch -p1

%build
%configure
%{__make}
	
%install
rm -rf $RPM_BUILD_ROOT
%{__install} -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_applnkdir}/Editors}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

echo ".so joe" > $RPM_BUILD_ROOT%{_mandir}/man1/jstar.1
echo ".so joe" > $RPM_BUILD_ROOT%{_mandir}/man1/jmacs.1
echo ".so joe" > $RPM_BUILD_ROOT%{_mandir}/man1/rjoe.1
echo ".so joe" > $RPM_BUILD_ROOT%{_mandir}/man1/jpico.1

install %{SOURCE1} $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_applnkdir}/Editors

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%dir %{_sysconfdir}
%config %{_sysconfdir}/*
%{_mandir}/man1/*
%{_applnkdir}/Editors/*
%{_pixmapsdir}/*
