%define		_status		alpha
%define		_pearname	OpenDocument
Summary:	%{_pearname} - read, create or modify office documents in OpenDocument format
Summary(pl.UTF-8):	%{_pearname} - odczyt, zapis i modyfikacja dokumentów zapisanych w formacie OpenDocument
Name:		php-pear-%{_pearname}
Version:	0.2.1
Release:	1
License:	PHP License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	e799ee3a6fb5af395c40cc65fcaf0877
URL:		http://pear.php.net/package/OpenDocument/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php(zip)
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OpenDocument is a package to read, create or modify office documents
in OpenDocument format.

OpenDocument format is a replacement for proprietary office formats
such as .doc or .xls. This package is a very useful tool for PHP
developers and another point to switch from proprietary office formats
to OpenDocument one, that means switching to open source software and
standards.

OpenDocument was developed as a project of Google Summer of Code 2006
Program. Package provides object oriented style for working with open
documents, a little similar to DOM as for XML.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
OpenDocument to pakiet do odczytu, zapisu oraz modyfikacji dokumentów
zapisanych w formacie OpenDocument.

Format OpenDocument jest zamiennikiem własnościowych formatów takich
jak .doc czy .xls. Pakiet ten jest szczególnie przydatnym narzędziem
dla programistów PHP planujących przejście na format OpenDocument, to
jest na standardy oraz oprogramowanie open source.

Pakiet OpenDocument został stworzony jako projekt programu Google
Summer of Code 2006. Pakiet ten dostarcza zorientowany obiektowo
interfejs do pracy nad dokumentami OpenDocument, podobny do DOM dla
XML.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

mv docs/%{_pearname}/examples .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_pear_dir},%{_examplesdir}/%{name}-%{version}}
%pear_package_install

cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/OpenDocument
%{php_pear_dir}/OpenDocument.php

%{php_pear_dir}/data/%{_pearname}

%{_examplesdir}/%{name}-%{version}
