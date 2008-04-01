%include	/usr/lib/rpm/macros.php
%define		_class		OpenDocument
%define		_subclass	%{nil}
%define		_status		alpha
%define		_pearname	OpenDocument
Summary:	%{_pearname} - read, create or modify office documents in OpenDocument format
Summary(pl.UTF-8):	%{_pearname} - odczyt, zapis i modyfikacja dokumentów zapisanych w formacie OpenDocument
Name:		php-pear-%{_pearname}
Version:	0.1.2
Release:	3
License:	PHP License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	75ec8b86f06aa44c5bf289c735661d9c
Patch0:		%{name}-paths.patch
URL:		http://pear.php.net/package/OpenDocument/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
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
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log %doc docs/OpenDocument/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/OpenDocument
%{php_pear_dir}/OpenDocument.php
