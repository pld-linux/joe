Summary:	Easy to use editor
Summary(de):	einfach handzuhabender Editor
Summary(fr):	éditeur facile à utiliser
Summary(pl):	£atwy w u¿yciu edytor tekstowy
Summary(tr):	Kolay kullanýmlý metin düzenleyici
Name:		joe
Version:	2.9.8pre1
%define		tar_version	2.9.8-pre1
Release:	2
License:	GPL
Group:		Applications/Editors
Source0:	http://prdownloads.sourceforge.net/joe-editor/%{name}-%{tar_version}.tgz
Source1:	%{name}.png
Source2:	%{name}.desktop
Source3:	%{name}-non-english-man-pages.tar.bz2
Patch0:		%{name}-pl_man.patch
Patch1:		%{name}-utag.diff
Icon:		joe.xpm
URL:		http://sourceforge.net/projects/joe-editor/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	ncurses-devel >= 5.0
BuildRoot:	%{tmpdir}/%{name}-%{tar_version}-root-%(id -u -n)

%define		_sysconfdir	/etc/joe

%description
Joe is a friendly and easy to use editor. It has a nice interface and
would be a good choice for a novice needing a text editor. It uses the
same WordStar keybindings which are also used by Borland's development
enbironment.

%description -l de
Joe ist ein bedienerfreundlicher, einfacher Editor mit attraktiver
Oberfläche. Eine gute Wahl für Neueinsteiger, die einen Texteditor
brauchen, benutzt er dieselben WordStar-Keybindings, die auch von
Borlands Enwicklungsumgebung verwendet werden.

%description -l fr
Joe est un éditeur de texte simple à utiliser. il à une interface
agréable et constitue un bon choix novice ayant besoin d'un éditeur de
texte. Il utilise les mêmes combinaisons de touches que WordStar, qui
sont aussi utilisées par les environnements de développement Borland.

%description -l pl
Joe jest ³atwym i przyjemnym w u¿yciu edytorem, ma ³adny interfejs i
mo¿e byæ dobrym wyborem dla pocz±tkuj±cych u¿ytkowników Linuxa. Joe
u¿ywa tej samej kombinacji klawiszy co WordStar i oprogramowae
Borland'a.

%description -l tr
Joe, küçük ve kullanýmý kolay bir metin düzenleyicisidir. Borland
firmasýnýn geliþtirme ortamýna alýþkýn olanlar ayný kýsayol tuþlarýný
kullanmaktan memnun olacaklardýr. Basitliði nedeni ile baþlayanlar
için en cok tavsiye edilen metin düzenleyicisidir.

%prep
%setup -q -a3 -n %{name}-%{tar_version}
%patch0 -p0

%build
rm -f missing
aclocal
autoconf
automake -a -c
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__install} -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_applnkdir}/Editors}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

for a in hu pl ; do
	install -d $RPM_BUILD_ROOT%{_mandir}/$a/man1
	install $a/man1/joe.1 $RPM_BUILD_ROOT%{_mandir}/$a/man1/
done

for a in "" hu pl ; do
	echo ".so joe" > $RPM_BUILD_ROOT%{_mandir}/$a/man1/jstar.1
	echo ".so joe" > $RPM_BUILD_ROOT%{_mandir}/$a/man1/jmacs.1
	echo ".so joe" > $RPM_BUILD_ROOT%{_mandir}/$a/man1/rjoe.1
	echo ".so joe" > $RPM_BUILD_ROOT%{_mandir}/$a/man1/jpico.1
done

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
%lang(hu) %{_mandir}/hu/man1/*
%lang(pl) %{_mandir}/pl/man1/*
%{_applnkdir}/Editors/*
%{_pixmapsdir}/*
