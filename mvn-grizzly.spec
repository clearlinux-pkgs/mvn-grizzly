#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-grizzly
Version  : 2.2.21
Release  : 4
URL      : https://github.com/javaee/grizzly/archive/2_2_21.tar.gz
Source0  : https://github.com/javaee/grizzly/archive/2_2_21.tar.gz
Source1  : https://repo1.maven.org/maven2/com/sun/grizzly/grizzly-framework/1.9.8/grizzly-framework-1.9.8.jar
Source2  : https://repo1.maven.org/maven2/com/sun/grizzly/grizzly-framework/1.9.8/grizzly-framework-1.9.8.pom
Source3  : https://repo1.maven.org/maven2/com/sun/grizzly/grizzly-http-servlet/1.9.8/grizzly-http-servlet-1.9.8.jar
Source4  : https://repo1.maven.org/maven2/com/sun/grizzly/grizzly-http-servlet/1.9.8/grizzly-http-servlet-1.9.8.pom
Source5  : https://repo1.maven.org/maven2/com/sun/grizzly/grizzly-http/1.9.8/grizzly-http-1.9.8.jar
Source6  : https://repo1.maven.org/maven2/com/sun/grizzly/grizzly-http/1.9.8/grizzly-http-1.9.8.pom
Source7  : https://repo1.maven.org/maven2/com/sun/grizzly/grizzly-portunif/1.9.8/grizzly-portunif-1.9.8.jar
Source8  : https://repo1.maven.org/maven2/com/sun/grizzly/grizzly-portunif/1.9.8/grizzly-portunif-1.9.8.pom
Source9  : https://repo1.maven.org/maven2/com/sun/grizzly/grizzly-project/1.9.8/grizzly-project-1.9.8.pom
Source10  : https://repo1.maven.org/maven2/com/sun/grizzly/grizzly-rcm/1.9.8/grizzly-rcm-1.9.8.jar
Source11  : https://repo1.maven.org/maven2/com/sun/grizzly/grizzly-rcm/1.9.8/grizzly-rcm-1.9.8.pom
Source12  : https://repo1.maven.org/maven2/com/sun/grizzly/grizzly-servlet-webserver/1.9.8/grizzly-servlet-webserver-1.9.8.jar
Source13  : https://repo1.maven.org/maven2/com/sun/grizzly/grizzly-servlet-webserver/1.9.8/grizzly-servlet-webserver-1.9.8.pom
Source14  : https://repo1.maven.org/maven2/com/sun/grizzly/grizzly-utils/1.9.8/grizzly-utils-1.9.8.jar
Source15  : https://repo1.maven.org/maven2/com/sun/grizzly/grizzly-utils/1.9.8/grizzly-utils-1.9.8.pom
Source16  : https://repo1.maven.org/maven2/org/glassfish/grizzly/grizzly-framework/2.2.21/grizzly-framework-2.2.21.jar
Source17  : https://repo1.maven.org/maven2/org/glassfish/grizzly/grizzly-framework/2.2.21/grizzly-framework-2.2.21.pom
Source18  : https://repo1.maven.org/maven2/org/glassfish/grizzly/grizzly-http-server/2.2.21/grizzly-http-server-2.2.21.jar
Source19  : https://repo1.maven.org/maven2/org/glassfish/grizzly/grizzly-http-server/2.2.21/grizzly-http-server-2.2.21.pom
Source20  : https://repo1.maven.org/maven2/org/glassfish/grizzly/grizzly-http-servlet/2.2.21/grizzly-http-servlet-2.2.21.jar
Source21  : https://repo1.maven.org/maven2/org/glassfish/grizzly/grizzly-http-servlet/2.2.21/grizzly-http-servlet-2.2.21.pom
Source22  : https://repo1.maven.org/maven2/org/glassfish/grizzly/grizzly-http/2.2.21/grizzly-http-2.2.21.jar
Source23  : https://repo1.maven.org/maven2/org/glassfish/grizzly/grizzly-http/2.2.21/grizzly-http-2.2.21.pom
Source24  : https://repo1.maven.org/maven2/org/glassfish/grizzly/grizzly-project/2.2.21/grizzly-project-2.2.21.pom
Source25  : https://repo1.maven.org/maven2/org/glassfish/grizzly/grizzly-rcm/2.2.21/grizzly-rcm-2.2.21.jar
Source26  : https://repo1.maven.org/maven2/org/glassfish/grizzly/grizzly-rcm/2.2.21/grizzly-rcm-2.2.21.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 CDDL-1.0 GPL-2.0
Requires: mvn-grizzly-data = %{version}-%{release}
BuildRequires : apache-ant
BuildRequires : buildreq-mvn

%description
The sample demonstrates how easy Grizzly HttpServer could be configured to process both HTTP and AJP requests.
All we need to do is register AjpAddOn on corresponding HTTP NetworkListener (see the code).

%package data
Summary: data components for the mvn-grizzly package.
Group: Data

%description data
data components for the mvn-grizzly package.


%prep
%setup -q -n grizzly-2_2_21

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/sun/grizzly/grizzly-framework/1.9.8
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/com/sun/grizzly/grizzly-framework/1.9.8/grizzly-framework-1.9.8.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/sun/grizzly/grizzly-framework/1.9.8
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/com/sun/grizzly/grizzly-framework/1.9.8/grizzly-framework-1.9.8.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/sun/grizzly/grizzly-http-servlet/1.9.8
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/com/sun/grizzly/grizzly-http-servlet/1.9.8/grizzly-http-servlet-1.9.8.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/sun/grizzly/grizzly-http-servlet/1.9.8
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/com/sun/grizzly/grizzly-http-servlet/1.9.8/grizzly-http-servlet-1.9.8.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/sun/grizzly/grizzly-http/1.9.8
cp %{SOURCE5} %{buildroot}/usr/share/java/.m2/repository/com/sun/grizzly/grizzly-http/1.9.8/grizzly-http-1.9.8.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/sun/grizzly/grizzly-http/1.9.8
cp %{SOURCE6} %{buildroot}/usr/share/java/.m2/repository/com/sun/grizzly/grizzly-http/1.9.8/grizzly-http-1.9.8.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/sun/grizzly/grizzly-portunif/1.9.8
cp %{SOURCE7} %{buildroot}/usr/share/java/.m2/repository/com/sun/grizzly/grizzly-portunif/1.9.8/grizzly-portunif-1.9.8.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/sun/grizzly/grizzly-portunif/1.9.8
cp %{SOURCE8} %{buildroot}/usr/share/java/.m2/repository/com/sun/grizzly/grizzly-portunif/1.9.8/grizzly-portunif-1.9.8.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/sun/grizzly/grizzly-project/1.9.8
cp %{SOURCE9} %{buildroot}/usr/share/java/.m2/repository/com/sun/grizzly/grizzly-project/1.9.8/grizzly-project-1.9.8.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/sun/grizzly/grizzly-rcm/1.9.8
cp %{SOURCE10} %{buildroot}/usr/share/java/.m2/repository/com/sun/grizzly/grizzly-rcm/1.9.8/grizzly-rcm-1.9.8.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/sun/grizzly/grizzly-rcm/1.9.8
cp %{SOURCE11} %{buildroot}/usr/share/java/.m2/repository/com/sun/grizzly/grizzly-rcm/1.9.8/grizzly-rcm-1.9.8.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/sun/grizzly/grizzly-servlet-webserver/1.9.8
cp %{SOURCE12} %{buildroot}/usr/share/java/.m2/repository/com/sun/grizzly/grizzly-servlet-webserver/1.9.8/grizzly-servlet-webserver-1.9.8.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/sun/grizzly/grizzly-servlet-webserver/1.9.8
cp %{SOURCE13} %{buildroot}/usr/share/java/.m2/repository/com/sun/grizzly/grizzly-servlet-webserver/1.9.8/grizzly-servlet-webserver-1.9.8.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/sun/grizzly/grizzly-utils/1.9.8
cp %{SOURCE14} %{buildroot}/usr/share/java/.m2/repository/com/sun/grizzly/grizzly-utils/1.9.8/grizzly-utils-1.9.8.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/sun/grizzly/grizzly-utils/1.9.8
cp %{SOURCE15} %{buildroot}/usr/share/java/.m2/repository/com/sun/grizzly/grizzly-utils/1.9.8/grizzly-utils-1.9.8.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/glassfish/grizzly/grizzly-framework/2.2.21
cp %{SOURCE16} %{buildroot}/usr/share/java/.m2/repository/org/glassfish/grizzly/grizzly-framework/2.2.21/grizzly-framework-2.2.21.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/glassfish/grizzly/grizzly-framework/2.2.21
cp %{SOURCE17} %{buildroot}/usr/share/java/.m2/repository/org/glassfish/grizzly/grizzly-framework/2.2.21/grizzly-framework-2.2.21.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/glassfish/grizzly/grizzly-http-server/2.2.21
cp %{SOURCE18} %{buildroot}/usr/share/java/.m2/repository/org/glassfish/grizzly/grizzly-http-server/2.2.21/grizzly-http-server-2.2.21.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/glassfish/grizzly/grizzly-http-server/2.2.21
cp %{SOURCE19} %{buildroot}/usr/share/java/.m2/repository/org/glassfish/grizzly/grizzly-http-server/2.2.21/grizzly-http-server-2.2.21.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/glassfish/grizzly/grizzly-http-servlet/2.2.21
cp %{SOURCE20} %{buildroot}/usr/share/java/.m2/repository/org/glassfish/grizzly/grizzly-http-servlet/2.2.21/grizzly-http-servlet-2.2.21.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/glassfish/grizzly/grizzly-http-servlet/2.2.21
cp %{SOURCE21} %{buildroot}/usr/share/java/.m2/repository/org/glassfish/grizzly/grizzly-http-servlet/2.2.21/grizzly-http-servlet-2.2.21.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/glassfish/grizzly/grizzly-http/2.2.21
cp %{SOURCE22} %{buildroot}/usr/share/java/.m2/repository/org/glassfish/grizzly/grizzly-http/2.2.21/grizzly-http-2.2.21.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/glassfish/grizzly/grizzly-http/2.2.21
cp %{SOURCE23} %{buildroot}/usr/share/java/.m2/repository/org/glassfish/grizzly/grizzly-http/2.2.21/grizzly-http-2.2.21.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/glassfish/grizzly/grizzly-project/2.2.21
cp %{SOURCE24} %{buildroot}/usr/share/java/.m2/repository/org/glassfish/grizzly/grizzly-project/2.2.21/grizzly-project-2.2.21.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/glassfish/grizzly/grizzly-rcm/2.2.21
cp %{SOURCE25} %{buildroot}/usr/share/java/.m2/repository/org/glassfish/grizzly/grizzly-rcm/2.2.21/grizzly-rcm-2.2.21.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/glassfish/grizzly/grizzly-rcm/2.2.21
cp %{SOURCE26} %{buildroot}/usr/share/java/.m2/repository/org/glassfish/grizzly/grizzly-rcm/2.2.21/grizzly-rcm-2.2.21.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/com/sun/grizzly/grizzly-framework/1.9.8/grizzly-framework-1.9.8.jar
/usr/share/java/.m2/repository/com/sun/grizzly/grizzly-framework/1.9.8/grizzly-framework-1.9.8.pom
/usr/share/java/.m2/repository/com/sun/grizzly/grizzly-http-servlet/1.9.8/grizzly-http-servlet-1.9.8.jar
/usr/share/java/.m2/repository/com/sun/grizzly/grizzly-http-servlet/1.9.8/grizzly-http-servlet-1.9.8.pom
/usr/share/java/.m2/repository/com/sun/grizzly/grizzly-http/1.9.8/grizzly-http-1.9.8.jar
/usr/share/java/.m2/repository/com/sun/grizzly/grizzly-http/1.9.8/grizzly-http-1.9.8.pom
/usr/share/java/.m2/repository/com/sun/grizzly/grizzly-portunif/1.9.8/grizzly-portunif-1.9.8.jar
/usr/share/java/.m2/repository/com/sun/grizzly/grizzly-portunif/1.9.8/grizzly-portunif-1.9.8.pom
/usr/share/java/.m2/repository/com/sun/grizzly/grizzly-project/1.9.8/grizzly-project-1.9.8.pom
/usr/share/java/.m2/repository/com/sun/grizzly/grizzly-rcm/1.9.8/grizzly-rcm-1.9.8.jar
/usr/share/java/.m2/repository/com/sun/grizzly/grizzly-rcm/1.9.8/grizzly-rcm-1.9.8.pom
/usr/share/java/.m2/repository/com/sun/grizzly/grizzly-servlet-webserver/1.9.8/grizzly-servlet-webserver-1.9.8.jar
/usr/share/java/.m2/repository/com/sun/grizzly/grizzly-servlet-webserver/1.9.8/grizzly-servlet-webserver-1.9.8.pom
/usr/share/java/.m2/repository/com/sun/grizzly/grizzly-utils/1.9.8/grizzly-utils-1.9.8.jar
/usr/share/java/.m2/repository/com/sun/grizzly/grizzly-utils/1.9.8/grizzly-utils-1.9.8.pom
/usr/share/java/.m2/repository/org/glassfish/grizzly/grizzly-framework/2.2.21/grizzly-framework-2.2.21.jar
/usr/share/java/.m2/repository/org/glassfish/grizzly/grizzly-framework/2.2.21/grizzly-framework-2.2.21.pom
/usr/share/java/.m2/repository/org/glassfish/grizzly/grizzly-http-server/2.2.21/grizzly-http-server-2.2.21.jar
/usr/share/java/.m2/repository/org/glassfish/grizzly/grizzly-http-server/2.2.21/grizzly-http-server-2.2.21.pom
/usr/share/java/.m2/repository/org/glassfish/grizzly/grizzly-http-servlet/2.2.21/grizzly-http-servlet-2.2.21.jar
/usr/share/java/.m2/repository/org/glassfish/grizzly/grizzly-http-servlet/2.2.21/grizzly-http-servlet-2.2.21.pom
/usr/share/java/.m2/repository/org/glassfish/grizzly/grizzly-http/2.2.21/grizzly-http-2.2.21.jar
/usr/share/java/.m2/repository/org/glassfish/grizzly/grizzly-http/2.2.21/grizzly-http-2.2.21.pom
/usr/share/java/.m2/repository/org/glassfish/grizzly/grizzly-project/2.2.21/grizzly-project-2.2.21.pom
/usr/share/java/.m2/repository/org/glassfish/grizzly/grizzly-rcm/2.2.21/grizzly-rcm-2.2.21.jar
/usr/share/java/.m2/repository/org/glassfish/grizzly/grizzly-rcm/2.2.21/grizzly-rcm-2.2.21.pom
