Summary:	Easy to use editor
Summary(de):	einfach handzuhabender Editor
Summary(es):	Editor fácil de usar
Summary(fr):	éditeur facile à utiliser
Summary(pl):	£atwy w u¿yciu edytor tekstowy
Summary(pt_BR):	Editor fácil de usar
Summary(ru):	ðÒÏÓÔÏÊ × ÉÓÐÏÌØÚÏ×ÁÎÉÉ ÔÅËÓÔÏ×ÙÊ ÒÅÄÁËÔÏÒ
Summary(tr):	Kolay kullanýmlý metin düzenleyici
Summary(uk):	ðÒÏÓÔÉÊ Õ ×ÉËÏÒÉÓÔÁÎÎ¦ ÔÅËÓÔÏ×ÉÊ ÒÅÄÁËÔÏÒ
Name:		joe
Version:	2.9.8pre1
%define		tar_version	2.9.8-pre1
Release:	6
License:	GPL
Group:		Applications/Editors
Source0:	http://dl.sourceforge.net/joe-editor/%{name}-%{tar_version}.tgz
Source1:	%{name}.png
Source2:	%{name}.desktop
Source3:	%{name}-non-english-man-pages.tar.bz2
Patch0:		%{name}-pl_man.patch
Patch1:		%{name}-isalnum.patch
Patch2:		%{name}-spaceblank.patch
Patch3:		%{name}-asis.patch
Patch4:		%{name}-dropsuid.patch
Icon:		joe.xpm
URL:		http://sourceforge.net/projects/joe-editor/
BuildRequires:	autoconf
BuildRequires:	automake
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
Oberfläche. Eine gute Wahl für Neueinsteiger, die einen Texteditor
brauchen, benutzt er dieselben WordStar-Keybindings, die auch von
Borlands Enwicklungsumgebung verwendet werden.

%description -l es
Joe es un editor amigable y fácil de usar. Posee una buena interface y
sería la mejor opción para un principiante que necesite de un editor.
Usa la misma combinación de teclas del WordStar, que también son
utilizadas por el ambiente de desarrollo de la Borland.

%description -l fr
Joe est un éditeur de texte simple à utiliser. il à une interface
agréable et constitue un bon choix novice ayant besoin d'un éditeur de
texte. Il utilise les mêmes combinaisons de touches que WordStar, qui
sont aussi utilisées par les environnements de développement Borland.

%description -l pl
Joe jest ³atwym i przyjemnym w u¿yciu edytorem, ma ³adny interfejs i
mo¿e byæ dobrym wyborem dla pocz±tkuj±cych u¿ytkowników Linuksa. Joe
u¿ywa tej samej kombinacji klawiszy co WordStar i oprogramowae
Borland'a.

%description -l ru
Joe - ÜÔÏ ÄÒÕÖÅÓÔ×ÅÎÎÙÊ, ÐÒÏÓÔÏÊ × ÉÓÐÏÌØÚÏ×ÁÎÉÉ ÔÅËÓÔÏ×ÙÊ ÒÅÄÁËÔÏÒ. õ
ÎÅÇÏ ÐÒÉÑÔÎÙÊ ÉÎÔÅÒÆÅÊÓ É ÔÁËÉÅ ÖÅ ÆÕÎËÃÉÉ ËÌÁ×ÉÛ, ËÁË É × ÓÉÓÔÅÍÁÈ
ÒÁÚÒÁÂÏÔËÉ ÐÒÏÇÒÁÍÍ ÆÉÒÍÙ Borland (ÔÁË ÎÁÚÙ×ÁÅÍÙÊ ÓÔÁÎÄÁÒÔ WordStar).

%description -l pt_BR
Joe é um editor amigável e fácil de usar. Possui uma boa interface e
seria a melhor opção para um novato precisando de um editor. Ele usa a
mesma combinação de teclas do WordStar que também são utilizadas pelo
ambiente de desenvolvimento da Borland.

%description -l tr
Joe, küçük ve kullanýmý kolay bir metin düzenleyicisidir. Borland
firmasýnýn geliþtirme ortamýna alýþkýn olanlar ayný kýsayol tuþlarýný
kullanmaktan memnun olacaklardýr. Basitliði nedeni ile baþlayanlar
için en cok tavsiye edilen metin düzenleyicisidir.

%description -l uk
Joe - ÃÅ ÄÒÕÖÎ¦Ê, ÐÒÏÓÔÉÊ Õ ×ÉËÏÒÉÓÔÁÎÎ¦ ÔÅËÓÔÏ×ÉÊ ÒÅÄÁËÔÏÒ. ÷¦Î ÍÁ¤
ÐÒÉ¤ÍÎÉÊ ¦ÎÔÅÒÆÅÊÓ ¦ ÔÁË¦ Ö ÓÁÍ¦ ÆÕÎËÃ¦§ ËÌÁ×¦Û, ÑË ¦ × ÓÉÓÔÅÍÁÈ
ÒÏÚÒÏÂËÉ ÐÒÏÇÒÁÍ Æ¦ÒÍÉ Borland (ÔÁË Ú×ÁÎÉÊ ÓÔÁÎÄÁÒÔ WordStar).

%prep
%setup -q -a3 -n %{name}-%{tar_version}
%patch0 -p0
%patch1 -p0
%patch2 -p0
%patch3 -p1
%patch4 -p1

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_applnkdir}/Editors}

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
%doc INFO LIST NEWS README TODO
%dir %{_sysconfdir}
%config %{_sysconfdir}/*
%{_mandir}/man1/*
%lang(hu) %{_mandir}/hu/man1/*
%lang(pl) %{_mandir}/pl/man1/*
%{_applnkdir}/Editors/*
%{_pixmapsdir}/*
