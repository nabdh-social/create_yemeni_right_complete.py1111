import os
import zipfile

print("=" * 60)
print("  جاري انشاء مشروع حقي كيمني")
print("=" * 60)

project_name = "my_yemeni_right"
base_dir = os.path.join(os.getcwd(), project_name)

# ========== انشاء المجلدات ==========
dirs = [
    "lib/core/theme",
    "lib/core/routes",
    "lib/screens/auth",
    "lib/screens/home",
    "lib/screens/laws",
    "lib/screens/consultations",
    "lib/screens/profile",
    "lib/screens/about",
    "lib/screens/faq",
    "android/app/src/main/kotlin/com/myemeniright/app",
    "android/gradle/wrapper",
    "assets/images",
    "assets/icons",
    "assets/fonts",
    "test",
]

for d in dirs:
    path = os.path.join(base_dir, d)
    os.makedirs(path, exist_ok=True)
    print(f"[OK] {d}")

def wf(relative_path, content):
    """Write file"""
    full_path = os.path.join(base_dir, relative_path)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"[OK] {relative_path}")

# ========== 1. pubspec.yaml ==========
wf("pubspec.yaml", """name: my_yemeni_right
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
  shared_preferences: ^2.2.2

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

# ========== 2. analysis_options.yaml ==========
wf("analysis_options.yaml", """include: package:flutter_lints/flutter.yaml

linter:
  rules:
    prefer_const_constructors: false
    prefer_const_literals_to_create_immutables: false
    avoid_print: false
""")

# ========== 3. lib/main.dart ==========
wf("lib/main.dart", """import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_localizations/flutter_localizations.dart';
import 'core/theme/app_theme.dart';
import 'core/routes/app_router.dart';

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
      supportedLocales: const [
        Locale('ar', 'YE'),
        Locale('en', 'US'),
      ],
      theme: AppTheme.lightTheme,
      darkTheme: AppTheme.darkTheme,
      themeMode: ThemeMode.system,
      routerConfig: AppRouter.router,
    );
  }
}
""")

# ========== 4. lib/core/theme/app_theme.dart ==========
wf("lib/core/theme/app_theme.dart", """import 'package:flutter/material.dart';
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
          textStyle: const TextStyle(fontSize: 16, fontWeight: FontWeight.bold),
        ),
      ),
      cardTheme: CardTheme(
        elevation: 2,
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.circular(12),
        ),
      ),
      inputDecorationTheme: InputDecorationTheme(
        filled: true,
        fillColor: Colors.white,
        border: OutlineInputBorder(
          borderRadius: BorderRadius.circular(12),
        ),
        enabledBorder: OutlineInputBorder(
          borderRadius: BorderRadius.circular(12),
          borderSide: const BorderSide(color: Colors.grey),
        ),
        focusedBorder: OutlineInputBorder(
          borderRadius: BorderRadius.circular(12),
          borderSide: const BorderSide(color: green, width: 2),
        ),
        contentPadding: const EdgeInsets.symmetric(
          horizontal: 16,
          vertical: 14,
        ),
      ),
      navigationBarTheme: const NavigationBarThemeData(
        indicatorColor: Color(0x331B5E20),
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
      elevatedButtonTheme: ElevatedButtonThemeData(
        style: ElevatedButton.styleFrom(
          backgroundColor: lightGreen,
          foregroundColor: Colors.black,
          padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 14),
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular(12),
          ),
        ),
      ),
      cardTheme: CardTheme(
        elevation: 2,
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.circular(12),
        ),
      ),
    );
  }
}
""")

# ========== 5. lib/core/routes/app_router.dart ==========
wf("lib/core/routes/app_router.dart", """import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import '../../screens/auth/login_screen.dart';
import '../../screens/auth/register_screen.dart';
import '../../screens/home/home_screen.dart';
import '../../screens/laws/laws_screen.dart';
import '../../screens/consultations/consultations_screen.dart';
import '../../screens/profile/profile_screen.dart';
import '../../screens/about/about_screen.dart';
import '../../screens/about/privacy_screen.dart';
import '../../screens/about/terms_screen.dart';
import '../../screens/faq/faq_screen.dart';

class AppRouter {
  static final GoRouter router = GoRouter(
    initialLocation: '/login',
    routes: [
      GoRoute(
        path: '/login',
        builder: (context, state) => const LoginScreen(),
      ),
      GoRoute(
        path: '/register',
        builder: (context, state) => const RegisterScreen(),
      ),
      GoRoute(
        path: '/',
        builder: (context, state) => const HomeScreen(),
      ),
      GoRoute(
        path: '/laws',
        builder: (context, state) => const LawsScreen(),
      ),
      GoRoute(
        path: '/consultations',
        builder: (context, state) => const ConsultationsScreen(),
      ),
      GoRoute(
        path: '/profile',
        builder: (context, state) => const ProfileScreen(),
      ),
      GoRoute(
        path: '/about',
        builder: (context, state) => const AboutScreen(),
      ),
      GoRoute(
        path: '/privacy',
        builder: (context, state) => const PrivacyScreen(),
      ),
      GoRoute(
        path: '/terms',
        builder: (context, state) => const TermsScreen(),
      ),
      GoRoute(
        path: '/faq',
        builder: (context, state) => const FaqScreen(),
      ),
    ],
    errorBuilder: (context, state) => Scaffold(
      appBar: AppBar(title: const Text('Error')),
      body: const Center(child: Text('Page not found')),
    ),
  );
}
""")

# ========== 6. lib/screens/auth/login_screen.dart ==========
wf("lib/screens/auth/login_screen.dart", """import 'package:flutter/material.dart';
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
  bool _obscure = true;

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
                const SizedBox(height: 6),
                Text(
                  'Login',
                  textAlign: TextAlign.center,
                  style: TextStyle(fontSize: 16, color: Colors.grey[600]),
                ),
                const SizedBox(height: 40),
                TextField(
                  controller: _emailCtrl,
                  keyboardType: TextInputType.emailAddress,
                  decoration: const InputDecoration(
                    labelText: 'Email',
                    prefixIcon: Icon(Icons.email_outlined),
                  ),
                ),
                const SizedBox(height: 16),
                TextField(
                  controller: _passCtrl,
                  obscureText: _obscure,
                  decoration: InputDecoration(
                    labelText: 'Password',
                    prefixIcon: const Icon(Icons.lock_outlined),
                    suffixIcon: IconButton(
                      icon: Icon(
                        _obscure ? Icons.visibility_off : Icons.visibility,
                      ),
                      onPressed: () => setState(() => _obscure = !_obscure),
                    ),
                  ),
                ),
                const SizedBox(height: 24),
                ElevatedButton(
                  onPressed: () => context.go('/'),
                  child: const Text('Login'),
                ),
                const SizedBox(height: 16),
                const Row(
                  children: [
                    Expanded(child: Divider()),
                    Padding(
                      padding: EdgeInsets.symmetric(horizontal: 16),
                      child: Text('OR'),
                    ),
                    Expanded(child: Divider()),
                  ],
                ),
                const SizedBox(height: 16),
                OutlinedButton.icon(
                  onPressed: () {},
                  icon: const Icon(Icons.phone_android),
                  label: const Text('Login with Phone'),
                  style: OutlinedButton.styleFrom(
                    padding: const EdgeInsets.symmetric(vertical: 14),
                  ),
                ),
                const SizedBox(height: 24),
                Row(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    const Text("Don't have an account? "),
                    TextButton(
                      onPressed: () => context.push('/register'),
                      child: const Text(
                        'Register',
                        style: TextStyle(fontWeight: FontWeight.bold),
                      ),
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

# ========== 7. lib/screens/auth/register_screen.dart ==========
wf("lib/screens/auth/register_screen.dart", """import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import '../../core/theme/app_theme.dart';

class RegisterScreen extends StatefulWidget {
  const RegisterScreen({super.key});
  @override
  State<RegisterScreen> createState() => _RegisterScreenState();
}

class _RegisterScreenState extends State<RegisterScreen> {
  final _nameCtrl = TextEditingController();
  final _emailCtrl = TextEditingController();
  final _phoneCtrl = TextEditingController();
  final _passCtrl = TextEditingController();
  String _userType = 'citizen';

  @override
  void dispose() {
    _nameCtrl.dispose();
    _emailCtrl.dispose();
    _phoneCtrl.dispose();
    _passCtrl.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Directionality(
      textDirection: TextDirection.rtl,
      child: Scaffold(
        appBar: AppBar(
          title: const Text('Create Account'),
          leading: IconButton(
            icon: const Icon(Icons.arrow_back),
            onPressed: () => context.pop(),
          ),
        ),
        body: SingleChildScrollView(
          padding: const EdgeInsets.all(24),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: [
              const Icon(Icons.person_add, size: 70, color: AppTheme.green),
              const SizedBox(height: 24),
              TextField(
                controller: _nameCtrl,
                decoration: const InputDecoration(
                  labelText: 'Full Name',
                  prefixIcon: Icon(Icons.person_outline),
                ),
              ),
              const SizedBox(height: 16),
              TextField(
                controller: _emailCtrl,
                keyboardType: TextInputType.emailAddress,
                decoration: const InputDecoration(
                  labelText: 'Email',
                  prefixIcon: Icon(Icons.email_outlined),
                ),
              ),
              const SizedBox(height: 16),
              TextField(
                controller: _phoneCtrl,
                keyboardType: TextInputType.phone,
                decoration: const InputDecoration(
                  labelText: 'Phone (+967)',
                  prefixIcon: Icon(Icons.phone_outlined),
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
              const SizedBox(height: 20),
              const Text(
                'Account Type',
                style: TextStyle(fontSize: 16, fontWeight: FontWeight.bold),
              ),
              Row(
                children: [
                  Expanded(
                    child: RadioListTile<String>(
                      title: const Text('Citizen'),
                      value: 'citizen',
                      groupValue: _userType,
                      onChanged: (v) => setState(() => _userType = v!),
                    ),
                  ),
                  Expanded(
                    child: RadioListTile<String>(
                      title: const Text('Lawyer'),
                      value: 'lawyer',
                      groupValue: _userType,
                      onChanged: (v) => setState(() => _userType = v!),
                    ),
                  ),
                ],
              ),
              const SizedBox(height: 24),
              ElevatedButton(
                onPressed: () => context.go('/'),
                child: const Text('Create Account'),
              ),
              const SizedBox(height: 16),
              Row(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  const Text('Already have an account? '),
                  TextButton(
                    onPressed: () => context.pop(),
                    child: const Text('Login'),
                  ),
                ],
              ),
            ],
          ),
        ),
      ),
    );
  }
}
""")

# ========== 8. lib/screens/home/home_screen.dart ==========
wf("lib/screens/home/home_screen.dart", """import 'package:flutter/material.dart';
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
          actions: [
            IconButton(
              icon: const Icon(Icons.notifications_outlined),
              onPressed: () {},
            ),
          ],
        ),
        SliverToBoxAdapter(
          child: Container(
            width: double.infinity,
            decoration: const BoxDecoration(
              gradient: LinearGradient(
                colors: [AppTheme.green, AppTheme.lightGreen],
                begin: Alignment.topRight,
                end: Alignment.bottomLeft,
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
                const SizedBox(height: 6),
                Text(
                  'Your comprehensive legal encyclopedia',
                  style: TextStyle(color: Colors.white.withOpacity(0.8), fontSize: 15),
                ),
                const SizedBox(height: 16),
                Row(
                  children: [
                    Expanded(
                      child: ElevatedButton.icon(
                        onPressed: () => context.push('/laws'),
                        icon: const Icon(Icons.search),
                        label: const Text('Search Laws'),
                        style: ElevatedButton.styleFrom(
                          backgroundColor: Colors.white,
                          foregroundColor: AppTheme.green,
                        ),
                      ),
                    ),
                    const SizedBox(width: 12),
                    ElevatedButton.icon(
                      onPressed: () => context.push('/consultations'),
                      icon: const Icon(Icons.add),
                      label: const Text('Consult'),
                    ),
                  ],
                ),
              ],
            ),
          ),
        ),
        SliverPadding(
          padding: const EdgeInsets.all(16),
          sliver: SliverGrid(
            gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
              crossAxisCount: 2,
              childAspectRatio: 1.3,
              crossAxisSpacing: 12,
              mainAxisSpacing: 12,
            ),
            delegate: SliverChildListDelegate([
              _QuickCard(Icons.gavel, 'Constitution', () => context.push('/laws')),
              _QuickCard(Icons.work, 'Labor Law', () => context.push('/laws')),
              _QuickCard(Icons.family_restroom, 'Personal Status', () => context.push('/laws')),
              _QuickCard(Icons.school, 'Education Law', () => context.push('/laws')),
              _QuickCard(Icons.security, 'Criminal Law', () => context.push('/laws')),
              _QuickCard(Icons.accessible, 'Disability Rights', () => context.push('/laws')),
            ]),
          ),
        ),
      ],
    );
  }
}

class _QuickCard extends StatelessWidget {
  final IconData icon;
  final String title;
  final VoidCallback onTap;

  const _QuickCard(this.icon, this.title, this.onTap);

  @override
  Widget build(BuildContext context) {
    return Card(
      child: InkWell(
        onTap: onTap,
        borderRadius: BorderRadius.circular(12),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Icon(icon, size: 36, color: AppTheme.green),
            const SizedBox(height: 8),
            Text(title, style: const TextStyle(fontWeight: FontWeight.bold)),
          ],
        ),
      ),
    );
  }
}

class _LawsTab extends StatelessWidget {
  const _LawsTab();
  @override
  Widget build(BuildContext context) {
    return ListView(
      padding: const EdgeInsets.all(16),
      children: [
        const Text('Laws', style: TextStyle(fontSize: 22, fontWeight: FontWeight.bold)),
        const SizedBox(height: 12),
        _LawItem('Constitution of Yemen', '150 articles'),
        _LawItem('Labor Law', '200 articles'),
        _LawItem('Personal Status Law', '180 articles'),
        _LawItem('Education Law', '120 articles'),
        _LawItem('Crimes & Penalties', '250 articles'),
      ],
    );
  }
}

class _LawItem extends StatelessWidget {
  final String title;
  final String sub;
  const _LawItem(this.title, this.sub);

  @override
  Widget build(BuildContext context) {
    return Card(
      margin: const EdgeInsets.only(bottom: 10),
      child: ListTile(
        leading: CircleAvatar(
          backgroundColor: AppTheme.green.withOpacity(0.1),
          child: const Icon(Icons.article, color: AppTheme.green),
        ),
        title: Text(title, style: const TextStyle(fontWeight: FontWeight.bold)),
        subtitle: Text(sub),
        trailing: const Icon(Icons.arrow_forward_ios, size: 14),
      ),
    );
  }
}

class _ConsultTab extends StatelessWidget {
  const _ConsultTab();
  @override
  Widget build(BuildContext context) {
    return Center(
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          const Icon(Icons.chat_bubble_outline, size: 64, color: Colors.grey),
          const SizedBox(height: 16),
          const Text('No consultations yet', style: TextStyle(fontSize: 18)),
          const SizedBox(height: 16),
          ElevatedButton.icon(
            onPressed: () => context.push('/consultations'),
            icon: const Icon(Icons.add),
            label: const Text('New Consultation'),
          ),
        ],
      ),
    );
  }
}

class _ProfileTab extends StatelessWidget {
  const _ProfileTab();
  @override
  Widget build(BuildContext context) {
    return ListView(
      padding: const EdgeInsets.all(16),
      children: [
        const SizedBox(height: 20),
        const CircleAvatar(
          radius: 50,
          backgroundColor: Color(0x1A1B5E20),
          child: Icon(Icons.person, size: 50, color: AppTheme.green),
        ),
        const SizedBox(height: 12),
        const Text('User', textAlign: TextAlign.center,
          style: TextStyle(fontSize: 22, fontWeight: FontWeight.bold)),
        const Text('Citizen', textAlign: TextAlign.center,
          style: TextStyle(color: Colors.grey)),
        const SizedBox(height: 24),
        _MenuItem(Icons.person_outline, 'Edit Profile', () {}),
        _MenuItem(Icons.bookmark_border, 'Saved Laws', () {}),
        _MenuItem(Icons.help_outline, 'FAQ', () => context.push('/faq')),
        _MenuItem(Icons.info_outline, 'About Us', () => context.push('/about')),
        _MenuItem(Icons.privacy_tip_outlined, 'Privacy', () => context.push('/privacy')),
        _MenuItem(Icons.description, 'Terms', () => context.push('/terms')),
        const Divider(height: 32),
        ListTile(
          leading: const Icon(Icons.logout, color: AppTheme.red),
          title: const Text('Logout', style: TextStyle(color: AppTheme.red)),
          onTap: () => context.go('/login'),
        ),
      ],
    );
  }
}

class _MenuItem extends StatelessWidget {
  final IconData icon;
  final String title;
  final VoidCallback onTap;
  const _MenuItem(this.icon, this.title, this.onTap);

  @override
  Widget build(BuildContext context) {
    return Card(
      margin: const EdgeInsets.only(bottom: 6),
      child: ListTile(
        leading: Icon(icon, color: AppTheme.green),
        title: Text(title),
        trailing: const Icon(Icons.arrow_forward_ios, size: 14),
        onTap: onTap,
      ),
    );
  }
}
""")

# ========== 9. lib/screens/laws/laws_screen.dart ==========
wf("lib/screens/laws/laws_screen.dart", """import 'package:flutter/material.dart';
import '../../core/theme/app_theme.dart';

class LawsScreen extends StatefulWidget {
  const LawsScreen({super.key});
  @override
  State<LawsScreen> createState() => _LawsScreenState();
}

class _LawsScreenState extends State<LawsScreen> {
  final _searchCtrl = TextEditingController();
  String _cat = 'all';

  final _categories = [
    {'id': 'all', 'name': 'All'},
    {'id': 'constitution', 'name': 'Constitution'},
    {'id': 'labor', 'name': 'Labor'},
    {'id': 'personal', 'name': 'Personal Status'},
    {'id': 'education', 'name': 'Education'},
    {'id': 'criminal', 'name': 'Criminal'},
  ];

  final _laws = [
    {'title': 'Constitution of Yemen', 'cat': 'constitution', 'count': 150},
    {'title': 'Labor Law', 'cat': 'labor', 'count': 200},
    {'title': 'Personal Status Law', 'cat': 'personal', 'count': 180},
    {'title': 'Education Law', 'cat': 'education', 'count': 120},
    {'title': 'Crimes & Penalties', 'cat': 'criminal', 'count': 250},
  ];

  @override
  void dispose() {
    _searchCtrl.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final filtered = _cat == 'all'
        ? _laws
        : _laws.where((l) => l['cat'] == _cat).toList();

    return Directionality(
      textDirection: TextDirection.rtl,
      child: Scaffold(
        appBar: AppBar(title: const Text('Legal Encyclopedia')),
        body: Column(
          children: [
            Padding(
              padding: const EdgeInsets.all(12),
              child: TextField(
                controller: _searchCtrl,
                decoration: InputDecoration(
                  hintText: 'Search laws...',
                  prefixIcon: const Icon(Icons.search),
                  filled: true,
                  fillColor: Colors.grey[100],
                  border: OutlineInputBorder(
                    borderRadius: BorderRadius.circular(12),
                    borderSide: BorderSide.none,
                  ),
                ),
                onChanged: (v) => setState(() {}),
              ),
            ),
            SizedBox(
              height: 50,
              child: ListView.builder(
                scrollDirection: Axis.horizontal,
                padding: const EdgeInsets.symmetric(horizontal: 12),
                itemCount: _categories.length,
                itemBuilder: (ctx, i) {
                  final c = _categories[i];
                  final sel = _cat == c['id'];
                  return Padding(
                    padding: const EdgeInsets.only(left: 8),
                    child: ChoiceChip(
                      label: Text(c['name']!),
                      selected: sel,
                      selectedColor: AppTheme.green.withOpacity(0.2),
                      onSelected: (_) => setState(() => _cat = c['id']!),
                    ),
                  );
                },
              ),
            ),
            const Divider(),
            Expanded(
              child: ListView.builder(
                padding: const EdgeInsets.all(12),
                itemCount: filtered.length,
                itemBuilder: (ctx, i) {
                  final law = filtered[i];
                  return Card(
                    margin: const EdgeInsets.only(bottom: 10),
                    child: ListTile(
                      leading: CircleAvatar(
                        backgroundColor: AppTheme.green.withOpacity(0.1),
                        child: const Icon(Icons.article, color: AppTheme.green),
                      ),
                      title: Text(law['title']!,
                        style: const TextStyle(fontWeight: FontWeight.bold)),
                      subtitle: Text('\${law['count']} articles'),
                      trailing: const Icon(Icons.arrow_forward_ios, size: 14),
                      onTap: () {
                        showDialog(
                          context: context,
                          builder: (ctx) => AlertDialog(
                            title: Text(law['title']!),
                            content: const Text('Law details will be shown here. Full legal text with articles and sections.'),
                            actions: [
                              TextButton(
                                onPressed: () => Navigator.pop(ctx),
                                child: const Text('Close'),
                              ),
                            ],
                          ),
                        );
                      },
                    ),
                  );
                },
              ),
            ),
          ],
        ),
      ),
    );
  }
}
""")

# ========== 10. lib/screens/consultations/consultations_screen.dart ==========
wf("lib/screens/consultations/consultations_screen.dart", """import 'package:flutter/material.dart';
import '../../core/theme/app_theme.dart';

class ConsultationsScreen extends StatefulWidget {
  const ConsultationsScreen({super.key});
  @override
  State<ConsultationsScreen> createState() => _ConsultationsScreenState();
}

class _ConsultationsScreenState extends State<ConsultationsScreen> {
  final _titleCtrl = TextEditingController();
  final _descCtrl = TextEditingController();
  String _category = 'Labor Law';

  final _cats = ['Labor Law', 'Personal Status', 'Criminal', 'Civil', 'Education', 'Other'];

  @override
  void dispose() {
    _titleCtrl.dispose();
    _descCtrl.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Directionality(
      textDirection: TextDirection.rtl,
      child: Scaffold(
        appBar: AppBar(title: const Text('New Consultation')),
        body: SingleChildScrollView(
          padding: const EdgeInsets.all(24),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: [
              TextField(
                controller: _titleCtrl,
                decoration: const InputDecoration(
                  labelText: 'Title',
                  hintText: 'e.g. Question about work contract',
                ),
              ),
              const SizedBox(height: 16),
              DropdownButtonFormField<String>(
                value: _category,
                decoration: const InputDecoration(labelText: 'Category'),
                items: _cats.map((c) => DropdownMenuItem(value: c, child: Text(c))).toList(),
                onChanged: (v) => setState(() => _category = v!),
              ),
              const SizedBox(height: 16),
              TextField(
                controller: _descCtrl,
                maxLines: 6,
                decoration: const InputDecoration(
                  labelText: 'Details',
                  hintText: 'Explain your question in detail...',
                ),
              ),
              const SizedBox(height: 24),
              ElevatedButton.icon(
                onPressed: () {
                  showDialog(
                    context: context,
                    builder: (ctx) => AlertDialog(
                      title: const Text('Sent Successfully'),
                      content: const Text('Your consultation has been sent. A lawyer will respond soon.'),
                      actions: [
                        TextButton(
                          onPressed: () {
                            Navigator.pop(ctx);
                            Navigator.pop(context);
                          },
                          child: const Text('OK'),
                        ),
                      ],
                    ),
                  );
                },
                icon: const Icon(Icons.send),
                label: const Text('Send Consultation'),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
""")

# ========== 11. lib/screens/profile/profile_screen.dart ==========
wf("lib/screens/profile/profile_screen.dart", """import 'package:flutter/material.dart';
import '../../core/theme/app_theme.dart';

class ProfileScreen extends StatelessWidget {
  const ProfileScreen({super.key});
  @override
  Widget build(BuildContext context) {
    return const Center(child: Text('Profile Screen'));
  }
}
""")

# ========== 12. lib/screens/about/about_screen.dart ==========
wf("lib/screens/about/about_screen.dart", """import 'package:flutter/material.dart';
import '../../core/theme/app_theme.dart';

class AboutScreen extends StatelessWidget {
  const AboutScreen({super.key});
  @override
  Widget build(BuildContext context) {
    return Directionality(
      textDirection: TextDirection.rtl,
      child: Scaffold(
        appBar: AppBar(title: const Text('About Us')),
        body: SingleChildScrollView(
          padding: const EdgeInsets.all(24),
          child: Column(
            children: [
              const Icon(Icons.balance, size: 80, color: AppTheme.green),
              const SizedBox(height: 20),
              const Text('Hakki Yamani', style: TextStyle(fontSize: 26, fontWeight: FontWeight.bold)),
              const SizedBox(height: 6),
              Text('Your Legal Encyclopedia', style: TextStyle(color: Colors.grey[600])),
              const SizedBox(height: 30),
              _section('Our Vision', 'To be the primary legal reference for every Yemeni citizen.'),
              const SizedBox(height: 16),
              _section('Our Mission', 'Provide reliable and simplified legal information, connecting citizens with specialized lawyers.'),
              const SizedBox(height: 16),
              _section('Our Goals', 'Spread legal culture. Provide comprehensive law database. Facilitate legal consultations.'),
              const SizedBox(height: 30),
              Text('Version 1.0.0', style: TextStyle(color: Colors.grey[500])),
            ],
          ),
        ),
      ),
    );
  }

  Widget _section(String title, String content) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(title, style: const TextStyle(fontSize: 18, fontWeight: FontWeight.bold, color: AppTheme.green)),
        const SizedBox(height: 6),
        Text(content, style: const TextStyle(fontSize: 15, height: 1.6)),
      ],
    );
  }
}
""")

# ========== 13. lib/screens/about/privacy_screen.dart ==========
wf("lib/screens/about/privacy_screen.dart", """import 'package:flutter/material.dart';

class PrivacyScreen extends StatelessWidget {
  const PrivacyScreen({super.key});
  @override
  Widget build(BuildContext context) {
    return Directionality(
      textDirection: TextDirection.rtl,
      child: Scaffold(
        appBar: AppBar(title: const Text('Privacy Policy')),
        body: SingleChildScrollView(
          padding: const EdgeInsets.all(24),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              const Text('Introduction', style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold)),
              const SizedBox(height: 8),
              const Text('Welcome to Hakki Yamani. We are committed to protecting your privacy. This policy explains how we collect, use, and protect your information.', style: TextStyle(fontSize: 15, height: 1.6)),
              const SizedBox(height: 20),
              const Text('Information We Collect', style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold)),
              const SizedBox(height: 8),
              const Text('We collect information you provide during registration: name, email, phone number. We may also collect usage data to improve our services.', style: TextStyle(fontSize: 15, height: 1.6)),
              const SizedBox(height: 20),
              const Text('Data Security', style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold)),
              const SizedBox(height: 8),
              const Text('We use advanced encryption to protect your data. We do not share your personal information with third parties without your consent.', style: TextStyle(fontSize: 15, height: 1.6)),
            ],
          ),
        ),
      ),
    );
  }
}
""")

# ========== 14. lib/screens/about/terms_screen.dart ==========
wf("lib/screens/about/terms_screen.dart", """import 'package:flutter/material.dart';

class TermsScreen extends StatelessWidget {
  const TermsScreen({super.key});
  @override
  Widget build(BuildContext context) {
    return Directionality(
      textDirection: TextDirection.rtl,
      child: Scaffold(
        appBar: AppBar(title: const Text('Terms of Use')),
        body: SingleChildScrollView(
          padding: const EdgeInsets.all(24),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              const Text('1. Acceptance', style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold)),
              const SizedBox(height: 6),
              const Text('By using Hakki Yamani, you agree to these terms. If you disagree, please do not use the app.', style: TextStyle(fontSize: 15, height: 1.6)),
              const SizedBox(height: 16),
              const Text('2. Nature of Service', style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold)),
              const SizedBox(height: 6),
              const Text('The app provides general legal information and consultations. It does not replace professional legal advice.', style: TextStyle(fontSize: 15, height: 1.6)),
              const SizedBox(height: 16),
              const Text('3. User Accounts', style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold)),
              const SizedBox(height: 6),
              const Text('You are responsible for keeping your account secure. Information provided must be accurate.', style: TextStyle(fontSize: 15, height: 1.6)),
            ],
          ),
        ),
      ),
    );
  }
}
""")

# ========== 15. lib/screens/faq/faq_screen.dart ==========
wf("lib/screens/faq/faq_screen.dart", """import 'package:flutter/material.dart';
import '../../core/theme/app_theme.dart';

class FaqScreen extends StatelessWidget {
  const FaqScreen({super.key});

  final _faqs = const [
    {'q': 'How long is maternity leave in Yemen?', 'a': 'According to Yemeni Labor Law, a working woman is entitled to 60 days of paid maternity leave.'},
    {'q': 'What are women inheritance rights?', 'a': 'Yemeni law and Islamic Sharia guarantee women their inheritance rights according to kinship rules.'},
    {'q': 'Can an employer fire without reason?', 'a': 'No. Arbitrary dismissal is prohibited. The worker has the right to claim compensation.'},
    {'q': 'What is the custody age in Yemen?', 'a': 'Custody is granted to the mother until the child reaches 7 for boys and 9 for girls.'},
    {'q': 'What are disability rights in education?', 'a': 'Yemeni law guarantees free and compulsory education for people with disabilities with appropriate integration.'},
  ];

  @override
  Widget build(BuildContext context) {
    return Directionality(
      textDirection: TextDirection.rtl,
      child: Scaffold(
        appBar: AppBar(title: const Text('FAQ')),
        body: ListView.builder(
          padding: const EdgeInsets.all(16),
          itemCount: _faqs.length,
          itemBuilder: (ctx, i) {
            final faq = _faqs[i];
            return Card(
              margin: const EdgeInsets.only(bottom: 10),
              child: ExpansionTile(
                leading: CircleAvatar(
                  backgroundColor: AppTheme.green.withOpacity(0.1),
                  child: const Icon(Icons.help_outline, color: AppTheme.green),
                ),
                title: Text(faq['q']!, style: const TextStyle(fontWeight: FontWeight.bold)),
                children: [
                  Padding(
                    padding: const EdgeInsets.fromLTRB(16, 0, 16, 16),
                    child: Text(faq['a']!, style: const TextStyle(fontSize: 15, height: 1.6)),
                  ),
                ],
              ),
            );
          },
        ),
      ),
    );
  }
}
""")

# ========== 16. android/app/src/main/AndroidManifest.xml ==========
wf("android/app/src/main/AndroidManifest.xml", """<manifest xmlns:android="http://schemas.android.com/apk/res/android">
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

# ========== 17. MainActivity.kt ==========
wf("android/app/src/main/kotlin/com/myemeniright/app/MainActivity.kt", """package com.myemeniright.app

import io.flutter.embedding.android.FlutterActivity

class MainActivity: FlutterActivity()
""")

# ========== 18. .gitignore ==========
wf(".gitignore", """.dart_tool/
.packages
.pub/
build/
.flutter-plugins
.flutter-plugins-dependencies
.idea/
.vscode/
*.iml
.DS_Store
""")

# ========== 19. README.md ==========
wf("README.md", """# Hakki Yamani - My Yemeni Right

## Requirements
- Flutter 3.10+
- Dart 3.0+

## Build