import os

print("=" * 60)
print("  Creating Hakki Yamani Project")
print("=" * 60)

project_name = "my_yemeni_right"
base_dir = os.path.join(os.getcwd(), project_name)

# Create directories
directories = [
    "lib/core/config/theme",
    "lib/core/services",
    "lib/features/auth/screens",
    "lib/features/home/screens",
    "lib/features/laws/screens",
    "lib/features/consultations/screens",
    "lib/features/profile/screens",
    "lib/features/about/screens",
    "lib/features/faq/screens",
    "lib/providers",
    "android/app/src/main/kotlin/com/myemeniright/app",
    "assets/images",
    "assets/icons",
    "assets/fonts",
]

for dir_path in directories:
    full_path = os.path.join(base_dir, dir_path)
    os.makedirs(full_path, exist_ok=True)
    print(f"OK: {dir_path}")

# File writing function
def write_file(relative_path, content):
    full_path = os.path.join(base_dir, relative_path)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"OK: {relative_path}")

# 1. pubspec.yaml
write_file("pubspec.yaml", """name: my_yemeni_right
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
write_file("lib/main.dart", """import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_localizations/flutter_localizations.dart';
import 'package:go_router/go_router.dart';
import 'core/config/theme/app_theme.dart';
import 'core/config/routes.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await SystemChrome.setPreferredOrientations([DeviceOrientation.portraitUp]);
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
        return Directionality(textDirection: TextDirection.rtl, child: child!);
      },
    );
  }
}
""")

# 3. app_theme.dart
write_file("lib/core/config/theme/app_theme.dart", """import 'package:flutter/material.dart';

class AppTheme {
  static const Color yemeniGreen = Color(0xFF1B5E20);
  static const Color yemeniRed = Color(0xFFC62828);
  static const Color yemeniWhite = Color(0xFFFFFFFF);
  static const Color goldAccent = Color(0xFFFFD700);
  static const Color lightGreen = Color(0xFF4CAF50);
  static const Color darkGreen = Color(0xFF1B5E20);
  static const Color backgroundLight = Color(0xFFF5F5F5);
  static const Color backgroundDark = Color(0xFF121212);

  static ThemeData get lightTheme {
    return ThemeData(
      useMaterial3: true,
      brightness: Brightness.light,
      primaryColor: yemeniGreen,
      scaffoldBackgroundColor: backgroundLight,
      colorScheme: const ColorScheme.light(
        primary: yemeniGreen,
        secondary: goldAccent,
        error: yemeniRed,
      ),
      appBarTheme: const AppBarTheme(
        backgroundColor: yemeniGreen,
        foregroundColor: yemeniWhite,
        elevation: 0,
        centerTitle: true,
      ),
      elevatedButtonTheme: ElevatedButtonThemeData(
        style: ElevatedButton.styleFrom(
          backgroundColor: yemeniGreen,
          foregroundColor: yemeniWhite,
          padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 16),
          shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
        ),
      ),
    );
  }

  static ThemeData get darkTheme {
    return ThemeData(
      useMaterial3: true,
      brightness: Brightness.dark,
      primaryColor: yemeniGreen,
      scaffoldBackgroundColor: backgroundDark,
      colorScheme: const ColorScheme.dark(
        primary: lightGreen,
        secondary: goldAccent,
        error: yemeniRed,
      ),
      appBarTheme: const AppBarTheme(
        backgroundColor: darkGreen,
        foregroundColor: yemeniWhite,
        elevation: 0,
        centerTitle: true,
      ),
    );
  }
}
""")

# 4. routes.dart
write_file("lib/core/config/routes.dart", """import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import '../../features/auth/screens/login_screen.dart';
import '../../features/auth/screens/register_screen.dart';
import '../../features/home/screens/home_screen.dart';
import '../../features/laws/screens/laws_list_screen.dart';
import '../../features/consultations/screens/consultations_list_screen.dart';
import '../../features/profile/screens/profile_screen.dart';
import '../../features/about/screens/about_screen.dart';
import '../../features/about/screens/privacy_screen.dart';
import '../../features/about/screens/terms_screen.dart';
import '../../features/faq/screens/faq_screen.dart';

class AppRouter {
  static final GoRouter router = GoRouter(
    initialLocation: '/login',
    routes: [
      GoRoute(path: '/login', builder: (context, state) => const LoginScreen()),
      GoRoute(path: '/register', builder: (context, state) => const RegisterScreen()),
      GoRoute(path: '/', builder: (context, state) => const HomeScreen()),
      GoRoute(path: '/laws', builder: (context, state) => const LawsListScreen()),
      GoRoute(path: '/consultations', builder: (context, state) => const ConsultationsListScreen()),
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

# 5. login_screen.dart
write_file("lib/features/auth/screens/login_screen.dart", """import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import '../../../core/config/theme/app_theme.dart';

class LoginScreen extends StatefulWidget {
  const LoginScreen({super.key});
  @override
  State<LoginScreen> createState() => _LoginScreenState();
}

class _LoginScreenState extends State<LoginScreen> {
  final _emailController = TextEditingController();
  final _passwordController = TextEditingController();
  bool _obscurePassword = true;

  @override
  void dispose() {
    _emailController.dispose();
    _passwordController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: SafeArea(
        child: SingleChildScrollView(
          padding: const EdgeInsets.all(24),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: [
              const SizedBox(height: 60),
              Icon(Icons.balance, size: 100, color: AppTheme.yemeniGreen),
              const SizedBox(height: 24),
              const Text('Hakki Yamani', textAlign: TextAlign.center,
                style: TextStyle(fontSize: 32, fontWeight: FontWeight.bold, color: AppTheme.yemeniGreen)),
              const SizedBox(height: 8),
              const Text('Login', textAlign: TextAlign.center,
                style: TextStyle(fontSize: 18, color: Colors.grey)),
              const SizedBox(height: 48),
              TextField(controller: _emailController,
                decoration: const InputDecoration(labelText: 'Email', prefixIcon: Icon(Icons.email_outlined))),
              const SizedBox(height: 16),
              TextField(controller: _passwordController, obscureText: _obscurePassword,
                decoration: InputDecoration(labelText: 'Password', prefixIcon: const Icon(Icons.lock_outlined),
                  suffixIcon: IconButton(
                    icon: Icon(_obscurePassword ? Icons.visibility_outlined : Icons.visibility_off_outlined),
                    onPressed: () => setState(() => _obscurePassword = !_obscurePassword),
                  ))),
              const SizedBox(height: 24),
              ElevatedButton(onPressed: () => context.go('/'), child: const Text('Login')),
              const SizedBox(height: 24),
              Row(mainAxisAlignment: MainAxisAlignment.center, children: [
                const Text("Don't have an account? "),
                TextButton(onPressed: () => context.push('/register'),
                  child: const Text('Register', style: TextStyle(fontWeight: FontWeight.bold))),
              ]),
            ],
          ),
        ),
      ),
    );
  }
}
""")

# 6. register_screen.dart
write_file("lib/features/auth/screens/register_screen.dart", """import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';

class RegisterScreen extends StatefulWidget {
  const RegisterScreen({super.key});
  @override
  State<RegisterScreen> createState() => _RegisterScreenState();
}

class _RegisterScreenState extends State<RegisterScreen> {
  final _nameController = TextEditingController();
  final _emailController = TextEditingController();
  final _passwordController = TextEditingController();

  @override
  void dispose() {
    _nameController.dispose();
    _emailController.dispose();
    _passwordController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Register')),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(24),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            TextField(controller: _nameController,
              decoration: const InputDecoration(labelText: 'Full Name')),
            const SizedBox(height: 16),
            TextField(controller: _emailController,
              decoration: const InputDecoration(labelText: 'Email')),
            const SizedBox(height: 16),
            TextField(controller: _passwordController, obscureText: true,
              decoration: const InputDecoration(labelText: 'Password')),
            const SizedBox(height: 24),
            ElevatedButton(onPressed: () => context.go('/'),
              child: const Text('Create Account')),
          ],
        ),
      ),
    );
  }
}
""")

# 7. home_screen.dart
write_file("lib/features/home/screens/home_screen.dart", """import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import '../../../core/config/theme/app_theme.dart';

class HomeScreen extends StatefulWidget {
  const HomeScreen({super.key});
  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  int _selectedIndex = 0;
  final List<Widget> _screens = const [HomeTab(), LawsTab(), ConsultationsTab(), ProfileTab()];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: _screens[_selectedIndex],
      bottomNavigationBar: NavigationBar(
        selectedIndex: _selectedIndex,
        onDestinationSelected: (index) => setState(() => _selectedIndex = index),
        destinations: const [
          NavigationDestination(icon: Icon(Icons.home_outlined), selectedIcon: Icon(Icons.home), label: 'Home'),
          NavigationDestination(icon: Icon(Icons.library_books_outlined), selectedIcon: Icon(Icons.library_books), label: 'Laws'),
          NavigationDestination(icon: Icon(Icons.chat_outlined), selectedIcon: Icon(Icons.chat), label: 'Consult'),
          NavigationDestination(icon: Icon(Icons.person_outline), selectedIcon: Icon(Icons.person), label: 'Profile'),
        ],
      ),
    );
  }
}

class HomeTab extends StatelessWidget {
  const HomeTab({super.key});
  @override
  Widget build(BuildContext context) {
    return CustomScrollView(slivers: [
      SliverAppBar(floating: true, title: const Text('Hakki Yamani')),
      SliverToBoxAdapter(child: Container(
        decoration: const BoxDecoration(
          gradient: LinearGradient(colors: [AppTheme.yemeniGreen, AppTheme.lightGreen]),
        ),
        padding: const EdgeInsets.all(24),
        child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
          const Text('Welcome', style: TextStyle(color: Colors.white, fontSize: 24, fontWeight: FontWeight.bold)),
          const SizedBox(height: 8),
          const Text('Your Legal Encyclopedia', style: TextStyle(color: Colors.white70, fontSize: 16)),
          const SizedBox(height: 16),
          ElevatedButton.icon(
            onPressed: () => context.push('/laws'),
            icon: const Icon(Icons.search),
            label: const Text('Search Laws'),
          ),
        ]),
      )),
    ]);
  }
}

class LawsTab extends StatelessWidget {
  const LawsTab({super.key});
  @override
  Widget build(BuildContext context) => const Center(child: Text('Laws'));
}

class ConsultationsTab extends StatelessWidget {
  const ConsultationsTab({super.key});
  @override
  Widget build(BuildContext context) => const Center(child: Text('Consultations'));
}

class ProfileTab extends StatelessWidget {
  const ProfileTab({super.key});
  @override
  Widget build(BuildContext context) => const Center(child: Text('Profile'));
}
""")

# 8. laws_list_screen.dart
write_file("lib/features/laws/screens/laws_list_screen.dart", """import 'package:flutter/material.dart';
import '../../../core/config/theme/app_theme.dart';

class LawsListScreen extends StatelessWidget {
  const LawsListScreen({super.key});
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Legal Encyclopedia')),
      body: ListView(
        padding: const EdgeInsets.all(16),
        children: [
          _buildLawCard('Constitution of Yemen', '150 articles'),
          _buildLawCard('Labor Law', '200 articles'),
          _buildLawCard('Personal Status Law', '180 articles'),
          _buildLawCard('Education Law', '120 articles'),
          _buildLawCard('Crimes and Penalties', '250 articles'),
        ],
      ),
    );
  }

  Widget _buildLawCard(String title, String subtitle) {
    return Card(
      margin: const EdgeInsets.only(bottom: 12),
      child: ListTile(
        leading: CircleAvatar(backgroundColor: AppTheme.yemeniGreen.withOpacity(0.1),
          child: const Icon(Icons.article, color: AppTheme.yemeniGreen)),
        title: Text(title, style: const TextStyle(fontWeight: FontWeight.bold)),
        subtitle: Text(subtitle),
        trailing: const Icon(Icons.arrow_forward_ios, size: 16),
      ),
    );
  }
}
""")

# 9. consultations_list_screen.dart
write_file("lib/features/consultations/screens/consultations_list_screen.dart", """import 'package:flutter/material.dart';

class ConsultationsListScreen extends StatelessWidget {
  const ConsultationsListScreen({super.key});
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Consultations')),
      body: const Center(child: Text('No consultations yet')),
      floatingActionButton: FloatingActionButton(
        onPressed: () {},
        child: const Icon(Icons.add),
      ),
    );
  }
}
""")

# 10. profile_screen.dart
write_file("lib/features/profile/screens/profile_screen.dart", """import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import '../../../core/config/theme/app_theme.dart';

class ProfileScreen extends StatelessWidget {
  const ProfileScreen({super.key});
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Profile')),
      body: ListView(
        children: [
          const SizedBox(height: 24),
          CircleAvatar(radius: 60, backgroundColor: AppTheme.yemeniGreen.withOpacity(0.1),
            child: const Icon(Icons.person, size: 60, color: AppTheme.yemeniGreen)),
          const SizedBox(height: 16),
          const Text('User', textAlign: TextAlign.center,
            style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold)),
          const SizedBox(height: 24),
          ListTile(leading: const Icon(Icons.info_outline),
            title: const Text('About Us'),
            onTap: () => context.push('/about')),
          ListTile(leading: const Icon(Icons.privacy_tip_outlined),
            title: const Text('Privacy'),
            onTap: () => context.push('/privacy')),
          ListTile(leading: const Icon(Icons.description),
            title: const Text('Terms'),
            onTap: () => context.push('/terms')),
          ListTile(leading: const Icon(Icons.help_outline),
            title: const Text('FAQ'),
            onTap: () => context.push('/faq')),
        ],
      ),
    );
  }
}
""")

# 11. about_screen.dart
write_file("lib/features/about/screens/about_screen.dart", """import 'package:flutter/material.dart';
import '../../../core/config/theme/app_theme.dart';

class AboutScreen extends StatelessWidget {
  const AboutScreen({super.key});
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('About Us')),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(24),
        child: Column(children: [
          Icon(Icons.balance, size: 80, color: AppTheme.yemeniGreen),
          const SizedBox(height: 24),
          const Text('Hakki Yamani', style: TextStyle(fontSize: 28, fontWeight: FontWeight.bold)),
          const SizedBox(height: 16),
          const Text('Your Legal Encyclopedia', style: TextStyle(fontSize: 16)),
          const SizedBox(height: 32),
          const Text('Our Vision: To be the primary legal reference for every Yemeni citizen',
            style: TextStyle(fontSize: 16, height: 1.6)),
          const SizedBox(height: 16),
          const Text('Our Mission: Provide reliable and simplified legal information',
            style: TextStyle(fontSize: 16, height: 1.6)),
          const SizedBox(height: 32),
          const Text('Version 1.0.0\\nAll rights reserved 2024',
            textAlign: TextAlign.center, style: TextStyle(color: Colors.grey)),
        ]),
      ),
    );
  }
}
""")

# 12. privacy_screen.dart
write_file("lib/features/about/screens/privacy_screen.dart", """import 'package:flutter/material.dart';

class PrivacyScreen extends StatelessWidget {
  const PrivacyScreen({super.key});
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Privacy Policy')),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(24),
        child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
          const Text('Introduction', style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold)),
          const SizedBox(height: 8),
          const Text('Welcome to Hakki Yamani. We are committed to protecting your privacy.',
            style: TextStyle(fontSize: 16, height: 1.6)),
        ]),
      ),
    );
  }
}
""")

# 13. terms_screen.dart
write_file("lib/features/about/screens/terms_screen.dart", """import 'package:flutter/material.dart';

class TermsScreen extends StatelessWidget {
  const TermsScreen({super.key});
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Terms of Use')),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(24),
        child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
          const Text('Terms and Conditions', style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold)),
          const SizedBox(height: 24),
          const Text('1. Acceptance', style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold)),
          const SizedBox(height: 8),
          const Text('By using Hakki Yamani, you agree to these terms.',
            style: TextStyle(fontSize: 16, height: 1.6)),
        ]),
      ),
    );
  }
}
""")

# 14. faq_screen.dart
write_file("lib/features/faq/screens/faq_screen.dart", """import 'package:flutter/material.dart';
import '../../../core/config/theme/app_theme.dart';

class FaqScreen extends StatelessWidget {
  const FaqScreen({super.key});
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('FAQ')),
      body: ListView(
        padding: const EdgeInsets.all(16),
        children: [
          _buildFaq('How long is maternity leave?', '60 days according to Yemeni Labor Law'),
          _buildFaq('What are women inheritance rights?', 'Guaranteed by law and Sharia'),
          _buildFaq('Can an employer fire without reason?', 'No, worker has right to compensation'),
        ],
      ),
    );
  }

  Widget _buildFaq(String question, String answer) {
    return Card(
      margin: const EdgeInsets.only(bottom: 12),
      child: ExpansionTile(
        leading: CircleAvatar(backgroundColor: AppTheme.yemeniGreen.withOpacity(0.1),
          child: const Icon(Icons.help_outline, color: AppTheme.yemeniGreen)),
        title: Text(question, style: const TextStyle(fontWeight: FontWeight.bold)),
        children: [Padding(padding: const EdgeInsets.all(16), child: Text(answer))],
      ),
    );
  }
}
""")

# 15. AndroidManifest.xml
write_file("android/app/src/main/AndroidManifest.xml", """<manifest xmlns:android="http://schemas.android.com/apk/res/android">
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

# 16. MainActivity.kt
write_file("android/app/src/main/kotlin/com/myemeniright/app/MainActivity.kt", """package com.myemeniright.app

import io.flutter.embedding.android.FlutterActivity

class MainActivity: FlutterActivity()
""")

# 17. .gitignore
write_file(".gitignore", """.dart_tool/
.packages
.pub/
build/
.flutter-plugins
.flutter-plugins-dependencies
.idea/
.vscode/
*.iml
.DS_Store
Thumbs.db
""")

# 18. README.md
write_file("README.md", """# Hakki Yamani - My Yemeni Right

## Requirements
- Flutter 3.10+
- Dart 3.0+

## Build
```bash
flutter pub get
flutter build apk --release
