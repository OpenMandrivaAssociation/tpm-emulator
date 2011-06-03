Summary:          TPM/MTM software emulator
Name:             tpm-emulator
Version:          0.7.2
Release:          0
License:          GPL
Group:            System/Kernel and hardware
URL:              http://tpm-emulator.berlios.de/
Source0:          http://download.berlios.de/tpm-emulator/tpm_emulator-%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-root
BuildRequires:  cmake
BuildRequires:  libgmp-devel

%description
An implementation of a software-based TPM/MTM emulator as well as of an
appropriate TCG Device Driver Library (TDDL).

The emulator enables not only the implementation of flexible and low-cost
test-beds and simulators but, in addition, provides programmers of trusted
systems with a powerful testing and debugging tool that can also be used
for educational purposes. Thanks to its portability and interoperability,
the TPM emulator runs on a variety of platforms (including Linux, Mac OS X,
and Windows) and is compatible with the most relevant software packages
and interfaces.

%package devel
Summary:          TPM/MTM software emulator development files
Group:  System/Libraries
Requires: %{name} = %{version}-%{release}

%description devel

%prep
%setup -q -n tpm_emulator-%{version}

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
export CXXFLAGS="%{optflags} -fno-strict-aliasing"
%cmake -DMTM_EMULATOR=ON
make %{_smp_mflags}

%install
cd build
make install DESTDIR=%{buildroot}

%if "%{_lib}" == "lib64"
    mv %{buildroot}/usr/lib %{buildroot}%{_libdir}
%endif


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%{_sysconfdir}/udev/rules.d/*.rules
/lib/modules/*/extra/tpmd_dev.ko
%{_bindir}/tpmd
%{_libdir}/libtddl.so.1.2
%{_libdir}/libtddl.so.1.2.0.7

%files devel
%defattr(-,root,root)
%{_includedir}/tddl.h
%{_libdir}/libtddl.a
%{_libdir}/libtddl.so
