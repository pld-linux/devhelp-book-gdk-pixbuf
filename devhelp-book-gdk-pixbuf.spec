Summary:	DevHelp book: gdk-pixbuf
Summary(pl):	Ksi±¿ka do DevHelpa o gdk-pixbuf
Name:		devhelp-book-gdk-pixbuf
Version:	1.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.devhelp.net/books/books/gdk-pixbuf.tar.gz
# Source0-md5:	4dd4805a078554de7318f8cc3c1bd689
URL:		http://www.devhelp.net/
Requires:	devhelp
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/share/devhelp

%description
DevHelp book about gdk-pixbuf.

%description -l pl
Ksi±¿ka do DevHelpa o gdk-pixbuf.

%prep
%setup -q -c -n gdk-pixbuf

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_prefix}/{books/gdkpixbuf,specs}

install book.devhelp $RPM_BUILD_ROOT%{_prefix}/specs/gdk-pixbuf.devhelp
install book/* $RPM_BUILD_ROOT%{_prefix}/books/gdkpixbuf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_prefix}/books/*
%{_prefix}/specs/*
