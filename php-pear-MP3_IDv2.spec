%define		status		alpha
%define		pearname	MP3_IDv2
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - read/write IDv2-Tags
Summary(pl.UTF-8):	%{pearname} - odczyt/zapis znaczników IDv2 w plikach MP3
Name:		php-pear-%{pearname}
Version:	0.1.7
Release:	1
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{pearname}-%{version}.tgz
# Source0-md5:	07b9f01fce17d11441fef254d3a21551
URL:		http://pear.php.net/package/MP3_IDv2/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.580
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The class offers methods for reading and writing information tags
(version 2) in MP3 files and other files in a MPEG format.

In PEAR status of this package is: %{status}.

%description -l pl.UTF-8
Klasa ta dostarcza metody do odczytu i zapisu znaczników
informacyjnych (w wersji drugiej) w plikach MP3 oraz innych plikach w
formacie MPEG.

Ta klasa ma w PEAR status: %{status}.

%prep
%pear_package_setup

# messed up dirs
# https://pear.php.net/bugs/bug.php?id=19590
mv .%{php_pear_dir}/MP3/MP3/* .%{php_pear_dir}/MP3

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/MP3_IDv2/{docs/examples/mp3testall.php,docs/LICENSE}
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/MP3/IDv2
