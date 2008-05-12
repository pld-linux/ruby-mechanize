Summary:	Library for automating interaction with web pages
Summary(pl.UTF-8):	Biblioteka do automatycznej interakcji ze stronami WWW
Name:		ruby-mechanize
Version:	0.7.6
Release:	1
License:	Ruby's
Group:		Development/Languages
Source0:	http://gems.rubyforge.org/gems/mechanize-%{version}.gem
# Source0-md5:	278a1df49f96b5ed7c2f5d4e15bf3002
URL:		http://mechanize.rubyforge.org/
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-devel
BuildRequires:	setup.rb = 3.3.1
%{?ruby_mod_ver_requires_eq}
#BuildArch:	noarch
Requires:	ruby-hpricot
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library for automating interaction with web pages.

%description -l pl.UTF-8
Biblioteka do automatycznej interakcji ze stronami WWW.

%prep
%setup -q -c
tar xf %{SOURCE0} -O data.tar.gz | tar xzv-
cp %{_datadir}/setup.rb .

%build
ruby setup.rb config \
	--rbdir=%{ruby_rubylibdir} \
	--sodir=%{ruby_archdir}

ruby setup.rb setup

rdoc --op rdoc lib
rdoc --ri --op ri lib

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_archdir},%{ruby_ridir}}

ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc rdoc
%{ruby_rubylibdir}/mechanize.rb
%{ruby_rubylibdir}/www
