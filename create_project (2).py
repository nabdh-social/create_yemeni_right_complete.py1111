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

# 2. lib/main.dart
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

# 3. lib/core/config/theme/app_theme.dart
write_file(f"{base_dir}/lib/core/config/theme/app_theme.dart", """import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

class AppTheme {
  static const Color green = Color(0xFF1B5E20);
  static const Color lightGreen = Color(0xFF4CAF50);
  static const Color red = Color(0xFFC62828);
  static const Color gold = Color(0xFFFFD700);
  static const Color bgLight = Color(0xFFF5F5F5);
  static const Color bgDark = Color(0xFF121212);

  static ThemeData get lightTheme {
    return ThemeData(
      useMaterial3: true,
      brightness: Brightness.light,
      primaryColor: green,
      scaffoldBackgroundColor: bgLight,
      colorScheme: const ColorScheme.light(
        primary: green,
        secondary: gold,
        error: red,
      ),
      appBarTheme: const AppBarTheme(
        backgroundColor: green,
        foregroundColor: Colors.white,
        elevation: 0,
        centerTitle: true,
        systemOverlayStyle: SystemUiOverlayStyle.light,
        titleTextStyle: TextStyle(
          fontSize: 20,
          fontWeight: FontWeight.bold,
          color: Colors.white,
        ),
      ),
      elevatedButtonTheme: ElevatedButtonThemeData(
        style: ElevatedButton.styleFrom(
          backgroundColor: green,
          foregroundColor: Colors.white,
          padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 14),
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular(12),
          ),
        ),
      ),
    );
  }

  static ThemeData get darkTheme {
    return ThemeData(
      useMaterial3: true,
      brightness: Brightness.dark,
      primaryColor: green,
      scaffoldBackgroundColor: bgDark,
      colorScheme: const ColorScheme.dark(
        primary: lightGreen,
        secondary: gold,
        error: red,
      ),
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

# 4. lib/core/config/routes.dart
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

# 5. lib/screens/auth/login_screen.dart
os.makedirs(f"{base_dir}/lib/screens/auth", exist_ok=True)
write_file(f"{base_dir}/lib/screens/auth/login_screen.dart", """import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import '../../core/theme/app_theme.dart';

class LoginScreen extends StatefulWidget {
  const LoginScreen({super.key});
  @override
  State<LoginScreen> createState() => _LoginScreenState();
}

class _LoginScreenState extends State<LoginScreen> {
  final _emailCtrl = TextEditingController();
  final _passCtrl = TextEditingController();

  @override
  void dispose() {
    _emailCtrl.dispose();
    _passCtrl.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Directionality(
      textDirection: TextDirection.rtl,
      child: Scaffold(
        body: SafeArea(
          child: SingleChildScrollView(
            padding: const EdgeInsets.all(24),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.stretch,
              children: [
                const SizedBox(height: 50),
                const Icon(Icons.balance, size: 100, color: AppTheme.green),
                const SizedBox(height: 20),
                const Text(
                  'Hakki Yamani',
                  textAlign: TextAlign.center,
                  style: TextStyle(
                    fontSize: 30,
                    fontWeight: FontWeight.bold,
                    color: AppTheme.green,
                  ),
                ),
                const SizedBox(height: 40),
                TextField(
                  controller: _emailCtrl,
                  decoration: const InputDecoration(
                    labelText: 'Email',
                    prefixIcon: Icon(Icons.email_outlined),
                  ),
                ),
                const SizedBox(height: 16),
                TextField(
                  controller: _passCtrl,
                  obscureText: true,
                  decoration: const InputDecoration(
                    labelText: 'Password',
                    prefixIcon: Icon(Icons.lock_outlined),
                  ),
                ),
                const SizedBox(height: 24),
                ElevatedButton(
                  onPressed: () => context.go('/'),
                  child: const Text('Login'),
                ),
                const SizedBox(height: 16),
                Row(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    const Text("Don't have an account? "),
                    TextButton(
                      onPressed: () => context.push('/register'),
                      child: const Text('Register'),
                    ),
                  ],
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}
""")

# 6. lib/screens/auth/register_screen.dart
write_file(f"{base_dir}/lib/screens/auth/register_screen.dart", """import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';

class RegisterScreen extends StatefulWidget {
  const RegisterScreen({super.key});
  @override
  State<RegisterScreen> createState() => _RegisterScreenState();
}

class _RegisterScreenState extends State<RegisterScreen> {
  final _nameCtrl = TextEditingController();
  final _emailCtrl = TextEditingController();
  final _passCtrl = TextEditingController();

  @override
  void dispose() {
    _nameCtrl.dispose();
    _emailCtrl.dispose();
    _passCtrl.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Directionality(
      textDirection: TextDirection.rtl,
      child: Scaffold(
        appBar: AppBar(title: const Text('Register')),
        body: SingleChildScrollView(
          padding: const EdgeInsets.all(24),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: [
              TextField(
                controller: _nameCtrl,
                decoration: const InputDecoration(labelText: 'Full Name'),
              ),
              const SizedBox(height: 16),
              TextField(
                controller: _emailCtrl,
                decoration: const InputDecoration(labelText: 'Email'),
              ),
              const SizedBox(height: 16),
              TextField(
                controller: _passCtrl,
                obscureText: true,
                decoration: const InputDecoration(labelText: 'Password'),
              ),
              const SizedBox(height: 24),
              ElevatedButton(
                onPressed: () => context.go('/'),
                child: const Text('Create Account'),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
""")

# 7. lib/screens/home/home_screen.dart
os.makedirs(f"{base_dir}/lib/screens/home", exist_ok=True)
write_file(f"{base_dir}/lib/screens/home/home_screen.dart", """import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import '../../core/theme/app_theme.dart';

class HomeScreen extends StatefulWidget {
  const HomeScreen({super.key});
  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  int _tab = 0;

  final _pages = const [
    _HomeTab(),
    _LawsTab(),
    _ConsultTab(),
    _ProfileTab(),
  ];

  @override
  Widget build(BuildContext context) {
    return Directionality(
      textDirection: TextDirection.rtl,
      child: Scaffold(
        body: _pages[_tab],
        bottomNavigationBar: NavigationBar(
          selectedIndex: _tab,
          onDestinationSelected: (i) => setState(() => _tab = i),
          destinations: const [
            NavigationDestination(
              icon: Icon(Icons.home_outlined),
              selectedIcon: Icon(Icons.home),
              label: 'Home',
            ),
            NavigationDestination(
              icon: Icon(Icons.library_books_outlined),
              selectedIcon: Icon(Icons.library_books),
              label: 'Laws',
            ),
            NavigationDestination(
              icon: Icon(Icons.chat_outlined),
              selectedIcon: Icon(Icons.chat),
              label: 'Consult',
            ),
            NavigationDestination(
              icon: Icon(Icons.person_outline),
              selectedIcon: Icon(Icons.person),
              label: 'Profile',
            ),
          ],
        ),
      ),
    );
  }
}

class _HomeTab extends StatelessWidget {
  const _HomeTab();

  @override
  Widget build(BuildContext context) {
    return CustomScrollView(
      slivers: [
        SliverAppBar(
          floating: true,
          title: const Text('Hakki Yamani'),
        ),
        SliverToBoxAdapter(
          child: Container(
            width: double.infinity,
            decoration: const BoxDecoration(
              gradient: LinearGradient(
                colors: [AppTheme.green, AppTheme.lightGreen],
              ),
            ),
            padding: const EdgeInsets.all(24),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                const Text(
                  'Welcome',
                  style: TextStyle(
                    color: Colors.white,
                    fontSize: 24,
                    fontWeight: FontWeight.bold,
                  ),
                ),
                const SizedBox(height: 16),
                ElevatedButton.icon(
                  onPressed: () => context.push('/laws'),
                  icon: const Icon(Icons.search),
                  label: const Text('Search Laws'),
                  style: ElevatedButton.styleFrom(
                    backgroundColor: Colors.white,
                    foregroundColor: AppTheme.green,
                  ),
                ),
              ],
            ),
          ),
        ),
      ],
    );
  }
}

class _LawsTab extends StatelessWidget {
  const _LawsTab();
  @override
  Widget build(BuildContext context) => const Center(child: Text('Laws'));
}

class _ConsultTab extends StatelessWidget {
  const _ConsultTab();
  @override
  Widget build(BuildContext context) => const Center(child: Text('Consultations'));
}

class _ProfileTab extends StatelessWidget {
  const _ProfileTab();
  @override
  Widget build(BuildContext context) => const Center(child: Text('Profile'));
}
""")

# 8. lib/screens/laws/laws_screen.dart
os.makedirs(f"{base_dir}/lib/screens/laws", exist_ok=True)
write_file(f"{base_dir}/lib/screens/laws/laws_screen.dart", """import 'package:flutter/material.dart';
import '../../core/theme/app_theme.dart';

class LawsScreen extends StatelessWidget {
  const LawsScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Directionality(
      textDirection: TextDirection.rtl,
      child: Scaffold(
        appBar: AppBar(title: const Text('Laws')),
        body: ListView(
          padding: const EdgeInsets.all(16),
          children: [
            _lawCard('Constitution', '150 articles'),
            _lawCard('Labor Law', '200 articles'),
            _lawCard('Personal Status', '180 articles'),
          ],
        ),
      ),
    );
  }

  Widget _lawCard(String title, String subtitle) {
    return Card(
      margin: const EdgeInsets.only(bottom: 10),
      child: ListTile(
        leading: CircleAvatar(
          backgroundColor: AppTheme.green.withOpacity(0.1),
          child: const Icon(Icons.article, color: AppTheme.green),
        ),
        title: Text(title),
        subtitle: Text(subtitle),
      ),
    );
  }
}
""")

# 9. lib/screens/consultations/consultations_screen.dart
os.makedirs(f"{base_dir}/lib/screens/consultations", exist_ok=True)
write_file(f"{base_dir}/lib/screens/consultations/consultations_screen.dart", """import 'package:flutter/material.dart';

class ConsultationsScreen extends StatelessWidget {
  const ConsultationsScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return const Directionality(
      textDirection: TextDirection.rtl,
      child: Scaffold(
        appBar: AppBar(title: Text('Consultations')),
        body: Center(child: Text('No consultations yet')),
      ),
    );
  }
}
""")

# 10. lib/screens/profile/profile_screen.dart
os.makedirs(f"{base_dir}/lib/screens/profile", exist_ok=True)
write_file(f"{base_dir}/lib/screens/profile/profile_screen.dart", """import 'package:flutter/material.dart';

class ProfileScreen extends StatelessWidget {
  const ProfileScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return const Directionality(
      textDirection: TextDirection.rtl,
      child: Scaffold(
        appBar: AppBar(title: Text('Profile')),
        body: Center(child: Text('Profile Screen')),
      ),
    );
  }
}
""")

# 11-14. About screens
os.makedirs(f"{base_dir}/lib/screens/about", exist_ok=True)
write_file(f"{base_dir}/lib/screens/about/about_screen.dart", """import 'package:flutter/material.dart';

class AboutScreen extends StatelessWidget {
  const AboutScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return const Directionality(
      textDirection: TextDirection.rtl,
      child: Scaffold(
        appBar: AppBar(title: Text('About')),
        body: Center(child: Text('About Us')),
      ),
    );
  }
}
""")

write_file(f"{base_dir}/lib/screens/about/privacy_screen.dart", """import 'package:flutter/material.dart';

class PrivacyScreen extends StatelessWidget {
  const PrivacyScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return const Directionality(
      textDirection: TextDirection.rtl,
      child: Scaffold(
        appBar: AppBar(title: Text('Privacy')),
        body: Center(child: Text('Privacy Policy')),
      ),
    );
  }
}
""")

write_file(f"{base_dir}/lib/screens/about/terms_screen.dart", """import 'package:flutter/material.dart';

class TermsScreen extends StatelessWidget {
  const TermsScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return const Directionality(
      textDirection: TextDirection.rtl,
      child: Scaffold(
        appBar: AppBar(title: Text('Terms')),
        body: Center(child: Text('Terms of Use')),
      ),
    );
  }
}
""")

# 15. FAQ screen
os.makedirs(f"{base_dir}/lib/screens/faq", exist_ok=True)
write_file(f"{base_dir}/lib/screens/faq/faq_screen.dart", """import 'package:flutter/material.dart';

class FaqScreen extends StatelessWidget {
  const FaqScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return const Directionality(
      textDirection: TextDirection.rtl,
      child: Scaffold(
        appBar: AppBar(title: Text('FAQ')),
        body: Center(child: Text('FAQ')),
      ),
    );
  }
}
""")

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
            <meta-data
              android:name="io.flutter.embedding.android.NormalTheme"
              android:resource="@style/NormalTheme"/>
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
.flutter-plugins
.flutter-plugins-dependencies
.idea/
.vscode/
*.iml
""")

# 19. README.md
write_file(f"{base_dir}/README.md", """# Hakki Yamani - My Yemeni Right

## Build
