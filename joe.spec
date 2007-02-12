# TODO:
#  - port / fix -spaceblank patch
#
Summary:	Easy to use editor
Summary(de.UTF-8):   Einfach handzuhabender Editor
Summary(es.UTF-8):   Editor fácil de usar
Summary(fr.UTF-8):   Éditeur facile à utiliser
Summary(pl.UTF-8):   Łatwy w użyciu edytor tekstowy
Summary(pt_BR.UTF-8):   Editor fácil de usar
Summary(ru.UTF-8):   Простой в использовании текстовый редактор
Summary(tr.UTF-8):   Kolay kullanımlı metin düzenleyici
Summary(uk.UTF-8):   Простий у використанні текстовий редактор
Name:		joe
Version:	3.5
Release:	1
Epoch:		1
License:	GPL
Group:		Applications/Editors
Source0:	http://dl.sourceforge.net/joe-editor/%{name}-%{version}.tar.gz
# Source0-md5:	9bdffecce7ef910feaa06452d48843de
Source1:	%{name}.png
Source2:	%{name}.desktop
Source3:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source3-md5:	47d050baa065ec9095d9d99217749abb
Patch0:		%{name}-pl_man.patch
Patch1:		%{name}-spaceblank.patch
Patch2:		%{name}-asis.patch
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

%description -l de.UTF-8
Joe ist ein bedienerfreundlicher, einfacher Editor mit attraktiver
Oberfläche. Eine gute Wahl für Neueinsteiger, die einen Texteditor
brauchen, er benutzt dieselben WordStar-Keybindings, die auch von
Borlands Enwicklungsumgebung verwendet werden.

%description -l es.UTF-8
Joe es un editor amigable y fácil de usar. Posee una buena interface y
sería la mejor opción para un principiante que necesite de un editor.
Usa la misma combinación de teclas del WordStar, que también son
utilizadas por el ambiente de desarrollo de la Borland.

%description -l fr.UTF-8
Joe est un éditeur de texte simple à utiliser. Il à une interface
agréable et constitue un bon choix novice ayant besoin d'un éditeur de
texte. Il utilise les mêmes combinaisons de touches que WordStar, qui
sont aussi utilisées par les environnements de développement Borland.

%description -l pl.UTF-8
Joe jest łatwym i przyjemnym w użyciu edytorem, ma ładny interfejs i
może być dobrym wyborem dla początkujących użytkowników Linuksa. Joe
używa tej samej kombinacji klawiszy co WordStar i oprogramowanie
Borland'a.

%description -l ru.UTF-8
Joe - это дружественный, простой в использовании текстовый редактор. У
него приятный интерфейс и такие же функции клавиш, как и в системах
разработки программ фирмы Borland (так называемый стандарт WordStar).

%description -l pt_BR.UTF-8
Joe é um editor amigável e fácil de usar. Possui uma boa interface e
seria a melhor opção para um novato precisando de um editor. Ele usa a
mesma combinação de teclas do WordStar que também são utilizadas pelo
ambiente de desenvolvimento da Borland.

%description -l tr.UTF-8
Joe, küçük ve kullanımı kolay bir metin düzenleyicisidir. Borland
firmasının geliştirme ortamına alışkın olanlar aynı kısayol tuşlarını
kullanmaktan memnun olacaklardır. Basitliği nedeni ile başlayanlar
için en cok tavsiye edilen metin düzenleyicisidir.

%description -l uk.UTF-8
Joe - це дружній, простий у використанні текстовий редактор. Він має
приємний інтерфейс і такі ж самі функції клавіш, як і в системах
розробки програм фірми Borland (так званий стандарт WordStar).

%prep
%setup -q -a3
%patch0 -p0
#%patch1 -p0
%patch2 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--sysconfdir=/etc
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

for a in hu pl ; do
	install -d $RPM_BUILD_ROOT%{_mandir}/$a/man1
	install $a/man1/joe.1 $RPM_BUILD_ROOT%{_mandir}/$a/man1
done

install -d $RPM_BUILD_ROOT%{_mandir}/ru/man1
install man/ru/joe.1 $RPM_BUILD_ROOT%{_mandir}/ru/man1

for a in "" hu pl ru ; do
	echo ".so joe" > $RPM_BUILD_ROOT%{_mandir}/$a/man1/jstar.1
	echo ".so joe" > $RPM_BUILD_ROOT%{_mandir}/$a/man1/jmacs.1
	echo ".so joe" > $RPM_BUILD_ROOT%{_mandir}/$a/man1/rjoe.1
	echo ".so joe" > $RPM_BUILD_ROOT%{_mandir}/$a/man1/jpico.1
done

install %{SOURCE1} $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LIST NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%dir %{_sysconfdir}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*
%{_mandir}/man1/*
%lang(hu) %{_mandir}/hu/man1/*
%lang(pl) %{_mandir}/pl/man1/*
%lang(ru) %{_mandir}/ru/man1/*
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
