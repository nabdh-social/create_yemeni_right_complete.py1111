import os
import urllib.request

print("=" * 60)
print("  Creating Hakki Yamani Project")
print("=" * 60)

project_name = "my_yemeni_right"
base_dir = os.path.join(os.getcwd(), project_name)

# Create directories
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
    f"{base_dir}/android/gradle/wrapper",
    f"{base_dir}/ios/Runner",
    f"{base_dir}/assets/images",
    f"{base_dir}/assets/icons",
    f"{base_dir}/assets/fonts",
    f"{base_dir}/test",
]

for dir_path in directories:
    os.makedirs(dir_path, exist_ok=True)
    print(f"OK: {dir_path.replace(base_dir + os.sep, '')}")

def write_file(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"OK: {os.path.basename(path)}")

# pubspec.yaml
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
  provider: ^6.0.5
  flutter_riverpod: ^2.4.0
  go_router: ^12.0.0
  firebase_core: ^2.24.0
  firebase_auth: ^4.15.0
  cloud_firestore: ^4.13.0
  hive: ^2.2.3
  hive_flutter: ^1.1.0
  path_provider: ^2.1.1
  cupertino_icons: ^1.0.6
  pin_code_fields: ^8.0.1
  image_picker: ^1.0.5
  permission_handler: ^11.0.1

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

# main.dart
write_file(f"{base_dir}/lib/main.dart", """import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_localizations/flutter_localizations.dart';
import 'package:provider/provider.dart';
import 'core/config/routes.dart';
import 'core/config/theme/app_theme.dart';

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

# app_theme.dart
write_file(f"{base_dir}/lib/core/config/theme/app_theme.dart", """import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

class AppTheme {
  static const Color yemeniGreen = Color(0xFF1B5E20);
  static const Color yemeniRed = Color(0xFFC62828);
  static const Color yemeniWhite = Color(0xFFFFFFFF);
  static const Color goldAccent = Color(0xFFFFD700);
  static const Color lightGreen = Color(0xFF4CAF50);
  static const Color darkGreen = Color(0xFF1B5E20);
  static const Color backgroundLight = Color(0xFFF5F5F5);
  static const Color backgroundDark = Color(0xFF121212);
  static const Color textSecondaryLight = Color(0xFF757575);
  static const Color textPrimaryDark = Color(0xFFFFFFFF);
  static const Color textSecondaryDark = Color(0xFFB0B0B0);

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
        systemOverlayStyle: SystemUiOverlayStyle.light,
        titleTextStyle: TextStyle(
          fontSize: 20,
          fontWeight: FontWeight.bold,
          color: yemeniWhite,
        ),
      ),
      elevatedButtonTheme: ElevatedButtonThemeData(
        style: ElevatedButton.styleFrom(
          backgroundColor: yemeniGreen,
          foregroundColor: yemeniWhite,
          padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 16),
          shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
          textStyle: const TextStyle(fontSize: 16, fontWeight: FontWeight.bold),
        ),
      ),
      textTheme: const TextTheme(
        headlineLarge: TextStyle(fontSize: 24, fontWeight: FontWeight.bold),
        titleLarge: TextStyle(fontSize: 20, fontWeight: FontWeight.bold),
        bodyLarge: TextStyle(fontSize: 16),
        bodyMedium: TextStyle(fontSize: 14, color: textSecondaryLight),
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
      textTheme: const TextTheme(
        headlineLarge: TextStyle(fontSize: 24, fontWeight: FontWeight.bold, color: textPrimaryDark),
        bodyLarge: TextStyle(fontSize: 16, color: textPrimaryDark),
        bodyMedium: TextStyle(fontSize: 14, color: textSecondaryDark),
      ),
    );
  }
}
""")

# routes.dart
write_file(f"{base_dir}/lib/core/config/routes.dart", """import 'package:flutter/material.dart';
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

# login_screen.dart
write_file(f"{base_dir}/lib/features/auth/screens/login_screen.dart", """import 'package:flutter/material.dart';
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
                style: TextStyle(fontSize: 18, color: AppTheme.textSecondaryLight)),
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

# register_screen.dart
write_file(f"{base_dir}/lib/features/auth/screens/register_screen.dart", """import 'package:flutter/material.dart';
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

# home_screen.dart
write_file(f"{base_dir}/lib/features/home/screens/home_screen.dart", """import 'package:flutter/material.dart';
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

# laws_list_screen.dart
write_file(f"{base_dir}/lib/features/laws/screens/laws_list_screen.dart", """import 'package:flutter/material.dart';
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

# consultations_list_screen.dart
write_file(f"{base_dir}/lib/features/consultations/screens/consultations_list_screen.dart", """import 'package:flutter/material.dart';

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

# profile_screen.dart
write_file(f"{base_dir}/lib/features/profile/screens/profile_screen.dart", """import 'package:flutter/material.dart';
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

# about_screen.dart
write_file(f"{base_dir}/lib/features/about/screens/about_screen.dart", """import 'package:flutter/material.dart';
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

# privacy_screen.dart
write_file(f"{base_dir}/lib/features/about/screens/privacy_screen.dart", """import 'package:flutter/material.dart';

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
          const SizedBox(height: 24),
          const Text('Information We Collect', style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold)),
          const SizedBox(height: 8),
          const Text('We collect information you provide during registration.', 
            style: TextStyle(fontSize: 16, height: 1.6)),
        ]),
      ),
    );
  }
}
""")

# terms_screen.dart
write_file(f"{base_dir}/lib/features/about/screens/terms_screen.dart", """import 'package:flutter/material.dart';

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

# faq_screen.dart
write_file(f"{base_dir}/lib/features/faq/screens/faq_screen.dart", """import 'package:flutter/material.dart';
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

# AndroidManifest.xml
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

# MainActivity.kt
write_file(f"{base_dir}/android/app/src/main/kotlin/com/myemeniright/app/MainActivity.kt", """package com.myemeniright.app

import io.flutter.embedding.android.FlutterActivity

class MainActivity: FlutterActivity()
""")

# .gitignore
write_file(f"{base_dir}/.gitignore", """.dart_tool/
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

# README.md
write_file(f"{base_dir}/README.md", """# Hakki Yamani - My Yemeni Right

## Requirements
- Flutter 3.10+
- Dart 3.0+

## Build
```bash
flutter pub get
flutter build apk --release
