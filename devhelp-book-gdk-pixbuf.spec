Summary:	DevHelp book: gdk-pixbuf
Summary(pl):	Ksi±¿ka do DevHelp'a o gdk-pixbuf
Name:		devhelp-book-gdk-pixbuf
Version:	1.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.devhelp.net/books/books/gdk-pixbuf.tar.gz
URL:		http://www.devhelp.net/
Requires:	devhelp
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6/share/devhelp/

%description
DevHelp book about gdk-pixbuf

%description -l pl
Ksi±¿ka do DevHelp o gdk-pixbuf

%prep
%setup -q -c gdk-pixbuf -n gdk-pixbuf

%build
mv -f book gdk-pixbuf
mv -f book.devhelp gdk-pixbuf.devhelp

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_prefix}/books/gdkpixbuf
install -d $RPM_BUILD_ROOT%{_prefix}/specs
install gdk-pixbuf.devhelp $RPM_BUILD_ROOT%{_prefix}/specs
install gdk-pixbuf/* $RPM_BUILD_ROOT%{_prefix}/books/gdkpixbuf

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
#%doc *.gz
%{_prefix}/books
%{_prefix}/specs
