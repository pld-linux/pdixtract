Summary:	Convert Pinnacle Disk Images to ISO9660 or extract files
Summary(pl):	Konwersja opraz�w dysk�w Pinnacle do ISO9660 i wyci�ganie plik�w
Name:		pdixtract
Version:	1.5
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://members.chello.se/jonas.thornqvist/PDITOOL.zip
# Source0-md5:	55c11c218e79208e0ea5c94b27ba5cd2
Patch0:		%{name}-LFS.patch
URL:		http://members.chello.se/jonas.thornqvist/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Convert Pinnacle Disk Images (i.e. .pdi file sets) to ISO9660 files
or extract files from the file sets.

%description -l pl
Narz�dzie do konwersji obraz�w dysk�w Pinnacle (zbior�w plik�w .pdi,
czyli Pinnacle Disk Images) do plik�w ISO9660 oraz wyci�gania plik�w
ze zbior�w plik�w.

%prep
%setup -qc
%patch0 -p0

%build
%{__cc} %{rpmldflags} %{rpmcflags} pdixtract.c -o pdixtract

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install pdixtract $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
