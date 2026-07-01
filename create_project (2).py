import os
import urllib.request

print("=" * 60)
print("  جاري إنشاء مشروع 'حقي كيمني'")
print("=" * 60)

project_name = "my_yemeni_right"
base_dir = os.path.join(os.getcwd(), project_name)

# إنشاء المجلدات
directories = [
    f"{base_dir}/lib/core/config/theme",
    f"{base_dir}/lib/core/services",
    f"{base_dir}/lib/features/auth/screens",
    f"{base_dir}/lib/features/home/screens",
    f"{base_dir}/lib/features/laws/screens",
    f"{base_dir}/lib/features/consultations/screens",
    f"{base_dir}/lib/features/profile/screens",
    f"{base_dir}/lib/features/lawyer/screens",
    f"{base_dir}/lib/features/about/screens",
    f"{base_dir}/lib/features/faq/screens",
    f"{base_dir}/lib/providers",
    f"{base_dir}/android/app/src/main/kotlin/com/myemeniright/app",
    f"{base_dir}/assets/images",
    f"{base_dir}/assets/icons",
    f"{base_dir}/assets/fonts",
]

for dir_path in directories:
    os.makedirs(dir_path, exist_ok=True)
    print(f"✓ {dir_path.replace(base_dir + os.sep, '')}")

def write_file(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✓ {os.path.basename(path)}")

# 1. pubspec.yaml
write_file(f"{base_dir}/pubspec.yaml", """name: my_yemeni_right
description: Hakki Yamani - Legal App
publish_to: 'none'
version: 1.0.0+1

environment:
  sdk: '>=3.0.0 <4.0.0'

dependencies:
  flutter:
    sdk: flutter
  flutter_localizations:
    sdk: flutter
  intl: ^0.18.1
  go_router: ^12.0.0
  cupertino_icons: ^1.0.6

dev_dependencies:
  flutter_test:
    sdk: flutter
  flutter_lints: ^3.0.1

flutter:
  uses-material-design: true
  assets:
    - assets/images/
    - assets/icons/
""")

# 2. main.dart
write_file(f"{base_dir}/lib/main.dart", """import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_localizations/flutter_localizations.dart';
import 'core/config/theme/app_theme.dart';
import 'core/config/routes.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await SystemChrome.setPreferredOrientations([
    DeviceOrientation.portraitUp,
  ]);
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp.router(
      title: 'Hakki Yamani',
      debugShowCheckedModeBanner: false,
      locale: const Locale('ar', 'YE'),
      localizationsDelegates: const [
        GlobalMaterialLocalizations.delegate,
        GlobalWidgetsLocalizations.delegate,
        GlobalCupertinoLocalizations.delegate,
      ],
      supportedLocales: const [Locale('ar', 'YE')],
      theme: AppTheme.lightTheme,
      darkTheme: AppTheme.darkTheme,
      themeMode: ThemeMode.system,
      routerConfig: AppRouter.router,
      builder: (context, child) {
        return Directionality(
          textDirection: TextDirection.rtl,
          child: child!,
        );
      },
    );
  }
}
""")

# 3. app_theme.dart
write_file(f"{base_dir}/lib/core/config/theme/app_theme.dart", """import 'package:flutter/material.dart';

class AppTheme {
  static const Color green = Color(0xFF1B5E20);
  static const Color lightGreen = Color(0xFF4CAF50);
  static const Color bgLight = Color(0xFFF5F5F5);

  static ThemeData get lightTheme {
    return ThemeData(
      useMaterial3: true,
      brightness: Brightness.light,
      primaryColor: green,
      scaffoldBackgroundColor: bgLight,
      appBarTheme: const AppBarTheme(
        backgroundColor: green,
        foregroundColor: Colors.white,
        elevation: 0,
        centerTitle: true,
      ),
    );
  }

  static ThemeData get darkTheme {
    return ThemeData(
      useMaterial3: true,
      brightness: Brightness.dark,
      primaryColor: green,
      scaffoldBackgroundColor: Colors.black,
      appBarTheme: const AppBarTheme(
        backgroundColor: Color(0xFF0D3B12),
        foregroundColor: Colors.white,
        elevation: 0,
        centerTitle: true,
      ),
    );
  }
}
""")

# 4. routes.dart
write_file(f"{base_dir}/lib/core/config/routes.dart", """import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import '../../features/auth/screens/login_screen.dart';
import '../../features/auth/screens/register_screen.dart';
import '../../features/home/screens/home_screen.dart';
import '../../features/laws/screens/laws_screen.dart';
import '../../features/consultations/consultations_screen.dart';
import '../../features/profile/profile_screen.dart';
import '../../features/about/about_screen.dart';
import '../../features/about/privacy_screen.dart';
import '../../features/about/terms_screen.dart';
import '../../features/faq/faq_screen.dart';

class AppRouter {
  static final GoRouter router = GoRouter(
    initialLocation: '/login',
    routes: [
      GoRoute(path: '/login', builder: (context, state) => const LoginScreen()),
      GoRoute(path: '/register', builder: (context, state) => const RegisterScreen()),
      GoRoute(path: '/', builder: (context, state) => const HomeScreen()),
      GoRoute(path: '/laws', builder: (context, state) => const LawsScreen()),
      GoRoute(path: '/consultations', builder: (context, state) => const ConsultationsScreen()),
      GoRoute(path: '/profile', builder: (context, state) => const ProfileScreen()),
      GoRoute(path: '/about', builder: (context, state) => const AboutScreen()),
      GoRoute(path: '/privacy', builder: (context, state) => const PrivacyScreen()),
      GoRoute(path: '/terms', builder: (context, state) => const TermsScreen()),
      GoRoute(path: '/faq', builder: (context, state) => const FaqScreen()),
    ],
    errorBuilder: (context, state) => Scaffold(
      appBar: AppBar(title: const Text('Error')),
      body: const Center(child: Text('Page not found')),
    ),
  );
}
""")

# 5-15. إنشاء الشاشات البسيطة
screens = {
    'login': """import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';

class LoginScreen extends StatelessWidget {
  const LoginScreen({super.key});
  @override
  Widget build(BuildContext context) {
    return Directionality(
      textDirection: TextDirection.rtl,
      child: Scaffold(
        body: Center(child: ElevatedButton(onPressed: () => context.go('/'), child: const Text('Login'))),
      ),
    );
  }
}
""",
    'register': """import 'package:flutter/material.dart';

class RegisterScreen extends StatelessWidget {
  const RegisterScreen({super.key});
  @override
  Widget build(BuildContext context) => const Directionality(textDirection: TextDirection.rtl, child: Scaffold(body: Center(child: Text('Register'))));
}
""",
    'home': """import 'package:flutter/material.dart';

class HomeScreen extends StatelessWidget {
  const HomeScreen({super.key});
  @override
  Widget build(BuildContext context) => const Directionality(textDirection: TextDirection.rtl, child: Scaffold(body: Center(child: Text('Home'))));
}
""",
    'laws': """import 'package:flutter/material.dart';

class LawsScreen extends StatelessWidget {
  const LawsScreen({super.key});
  @override
  Widget build(BuildContext context) => const Directionality(textDirection: TextDirection.rtl, child: Scaffold(body: Center(child: Text('Laws'))));
}
""",
    'consultations': """import 'package:flutter/material.dart';

class ConsultationsScreen extends StatelessWidget {
  const ConsultationsScreen({super.key});
  @override
  Widget build(BuildContext context) => const Directionality(textDirection: TextDirection.rtl, child: Scaffold(body: Center(child: Text('Consultations'))));
}
""",
    'profile': """import 'package:flutter/material.dart';

class ProfileScreen extends StatelessWidget {
  const ProfileScreen({super.key});
  @override
  Widget build(BuildContext context) => const Directionality(textDirection: TextDirection.rtl, child: Scaffold(body: Center(child: Text('Profile'))));
}
""",
    'about': """import 'package:flutter/material.dart';

class AboutScreen extends StatelessWidget {
  const AboutScreen({super.key});
  @override
  Widget build(BuildContext context) => const Directionality(textDirection: TextDirection.rtl, child: Scaffold(body: Center(child: Text('About'))));
}
""",
    'privacy': """import 'package:flutter/material.dart';

class PrivacyScreen extends StatelessWidget {
  const PrivacyScreen({super.key});
  @override
  Widget build(BuildContext context) => const Directionality(textDirection: TextDirection.rtl, child: Scaffold(body: Center(child: Text('Privacy'))));
}
""",
    'terms': """import 'package:flutter/material.dart';

class TermsScreen extends StatelessWidget {
  const TermsScreen({super.key});
  @override
  Widget build(BuildContext context) => const Directionality(textDirection: TextDirection.rtl, child: Scaffold(body: Center(child: Text('Terms'))));
}
""",
    'faq': """import 'package:flutter/material.dart';

class FaqScreen extends StatelessWidget {
  const FaqScreen({super.key});
  @override
  Widget build(BuildContext context) => const Directionality(textDirection: TextDirection.rtl, child: Scaffold(body: Center(child: Text('FAQ'))));
}
""",
}

for screen_name, screen_code in screens.items():
    if screen_name in ['login', 'register']:
        os.makedirs(f"{base_dir}/lib/features/auth/screens", exist_ok=True)
        write_file(f"{base_dir}/lib/features/auth/screens/{screen_name}_screen.dart", screen_code)
    else:
        folder = screen_name if screen_name != 'consultations' else 'consultations'
        os.makedirs(f"{base_dir}/lib/features/{folder}/screens", exist_ok=True)
        write_file(f"{base_dir}/lib/features/{folder}/{screen_name}_screen.dart", screen_code)

# 16. AndroidManifest.xml
write_file(f"{base_dir}/android/app/src/main/AndroidManifest.xml", """<manifest xmlns:android="http://schemas.android.com/apk/res/android">
    <uses-permission android:name="android.permission.INTERNET"/>
    <application
        android:label="Hakki Yamani"
        android:name="\${applicationName}"
        android:icon="@mipmap/ic_launcher">
        <activity
            android:name=".MainActivity"
            android:exported="true"
            android:launchMode="singleTop"
            android:theme="@style/LaunchTheme"
            android:configChanges="orientation|keyboardHidden|keyboard|screenSize|smallestScreenSize|locale|layoutDirection|fontScale|screenLayout|density|uiMode"
            android:hardwareAccelerated="true"
            android:windowSoftInputMode="adjustResize">
            <meta-data android:name="io.flutter.embedding.android.NormalTheme" android:resource="@style/NormalTheme"/>
            <intent-filter>
                <action android:name="android.intent.action.MAIN"/>
                <category android:name="android.intent.category.LAUNCHER"/>
            </intent-filter>
        </activity>
        <meta-data android:name="flutterEmbedding" android:value="2"/>
    </application>
</manifest>
""")

# 17. MainActivity.kt
write_file(f"{base_dir}/android/app/src/main/kotlin/com/myemeniright/app/MainActivity.kt", """package com.myemeniright.app

import io.flutter.embedding.android.FlutterActivity

class MainActivity: FlutterActivity()
""")

# 18. .gitignore
write_file(f"{base_dir}/.gitignore", """.dart_tool/
.packages
.pub/
build/
""")

# 19. README.md
write_file(f"{base_dir}/README.md", """# Hakki Yamani

## Build
```bash
flutter pub get
flutter build apk --release
