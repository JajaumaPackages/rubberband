Name:           rubberband
Version:        1.0.1
Release:        1%{?dist}
Summary:        Audio time-stretching and pitch-shifting library

Group:          System Environment/Libraries
License:        GPLv2+
URL:            http://www.breakfastquay.com/rubberband/
Source0:        http://www.breakfastquay.com/rubberband/files/rubberband-%{version}.tar.bz2
Patch0:         rubberband-1.0.1-gcc43.patch
Patch1:         rubberband-1.0.1-destdir.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  fftw-devel libsamplerate-devel libsndfile-devel
BuildRequires:  ladspa-devel vamp-plugin-sdk-devel
#Requires:       

%description
Rubber Band is a library and utility program that permits you to change the
tempo and pitch of an audio recording independently of one another. 


%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q
%patch0 -p1 -b .gcc43
%patch1 -p1 -b .destdir


%build
%configure --disable-static
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


%clean
rm -rf $RPM_BUILD_ROOT


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%doc COPYING README
%{_bindir}/rubberband
%{_libdir}/*.so.*
%{_libdir}/ladspa/ladspa-rubberband.*
%{_libdir}/vamp/vamp-rubberband.*

%files devel
%defattr(-,root,root,-)
%doc
%{_includedir}/*
%{_libdir}/*.a
%{_libdir}/*.so
%{_libdir}/pkgconfig/rubberband.pc


%changelog
* Sun Mar 30 2008 Michel Salim <michel.sylvan@gmail.com> - 1.0.1-1
- Initial package

