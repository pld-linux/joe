Summary:	Easy to use editor
Summary(de):	einfach handzuhabender Editor
Summary(es):	Editor f�cil de usar
Summary(fr):	�diteur facile � utiliser
Summary(pl):	�atwy w u�yciu edytor tekstowy
Summary(pt_BR):	Editor f�cil de usar
Summary(ru):	������� � ������������� ��������� ��������
Summary(tr):	Kolay kullan�ml� metin d�zenleyici
Summary(uk):	������� � ����������Φ ��������� ��������
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
Oberfl�che. Eine gute Wahl f�r Neueinsteiger, die einen Texteditor
brauchen, benutzt er dieselben WordStar-Keybindings, die auch von
Borlands Enwicklungsumgebung verwendet werden.

%description -l es
Joe es un editor amigable y f�cil de usar. Posee una buena interface y
ser�a la mejor opci�n para un principiante que necesite de un editor.
Usa la misma combinaci�n de teclas del WordStar, que tambi�n son
utilizadas por el ambiente de desarrollo de la Borland.

%description -l fr
Joe est un �diteur de texte simple � utiliser. il � une interface
agr�able et constitue un bon choix novice ayant besoin d'un �diteur de
texte. Il utilise les m�mes combinaisons de touches que WordStar, qui
sont aussi utilis�es par les environnements de d�veloppement Borland.

%description -l pl
Joe jest �atwym i przyjemnym w u�yciu edytorem, ma �adny interfejs i
mo�e by� dobrym wyborem dla pocz�tkuj�cych u�ytkownik�w Linuksa. Joe
u�ywa tej samej kombinacji klawiszy co WordStar i oprogramowae
Borland'a.

%description -l ru
Joe - ��� �������������, ������� � ������������� ��������� ��������. �
���� �������� ��������� � ����� �� ������� ������, ��� � � ��������
���������� �������� ����� Borland (��� ���������� �������� WordStar).

%description -l pt_BR
Joe � um editor amig�vel e f�cil de usar. Possui uma boa interface e
seria a melhor op��o para um novato precisando de um editor. Ele usa a
mesma combina��o de teclas do WordStar que tamb�m s�o utilizadas pelo
ambiente de desenvolvimento da Borland.

%description -l tr
Joe, k���k ve kullan�m� kolay bir metin d�zenleyicisidir. Borland
firmas�n�n geli�tirme ortam�na al��k�n olanlar ayn� k�sayol tu�lar�n�
kullanmaktan memnun olacaklard�r. Basitli�i nedeni ile ba�layanlar
i�in en cok tavsiye edilen metin d�zenleyicisidir.

%description -l uk
Joe - �� ����Φ�, ������� � ����������Φ ��������� ��������. ��� ���
��ɤ���� ��������� � ��˦ � ��ͦ ����æ� ���צ�, �� � � ��������
�������� ������� Ʀ��� Borland (��� ������ �������� WordStar).

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
