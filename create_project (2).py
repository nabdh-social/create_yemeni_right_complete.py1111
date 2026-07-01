import os
import urllib.request

print("=" * 60)
print("  Creating Hakki Yamani Project (FIXED)")
print("=" * 60)

project_name = "my_yemeni_right"
base_dir = os.path.join(os.getcwd(), project_name)

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

print("\nGenerating logo...")
try:
    from PIL import Image, ImageDraw
    size = 1024
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    yemeni_green = (27, 94, 32, 255)
    yemeni_red = (198, 40, 40, 255)
    yemeni_white = (255, 255, 255, 255)
    yemeni_black = (33, 33, 33, 255)
    gold = (255, 215, 0, 255)
    shield_points = [
        (size // 2, 80),
        (size - 120, 150),
        (size - 120, size // 2 + 100),
        (size // 2, size - 80),
        (120, size // 2 + 100),
        (120, 150),
    ]
    draw.polygon(shield_points, fill=yemeni_green, outline=gold, width=15)
    stripe_height = (size - 260) // 3
    draw.rectangle([140, 170, size - 140, 170 + stripe_height], fill=yemeni_red)
    draw.rectangle([140, 170 + stripe_height, size - 140, 170 + stripe_height * 2], fill=yemeni_white)
    draw.rectangle([140, 170 + stripe_height * 2, size - 140, 170 + stripe_height * 3], fill=yemeni_black)
    center_x = size // 2
    draw.rectangle([center_x - 15, 280, center_x + 15, 700], fill=gold, outline=yemeni_black, width=3)
    draw.rectangle([center_x - 120, 700, center_x + 120, 730], fill=gold, outline=yemeni_black, width=3)
    draw.rectangle([center_x - 150, 730, center_x + 150, 760], fill=gold, outline=yemeni_black, width=3)
    draw.rectangle([180, 280, size - 180, 310], fill=gold, outline=yemeni_black, width=3)
    draw.ellipse([center_x - 25, 240, center_x + 25, 290], fill=gold, outline=yemeni_black, width=3)
    draw.line([220, 310, 220, 500], fill=gold, width=8)
    draw.line([180, 500, 260, 500], fill=gold, width=8)
    draw.polygon([(180, 500), (260, 500), (240, 620), (200, 620)], fill=gold, outline=yemeni_black, width=3)
    draw.line([size - 220, 310, size - 220, 500], fill=gold, width=8)
    draw.line([size - 260, 500, size - 180, 500], fill=gold, width=8)
    draw.polygon([(size - 260, 500), (size - 180, 500), (size - 200, 620), (size - 240, 620)], fill=gold, outline=yemeni_black, width=3)
    draw.ellipse([170, 270, 230, 330], fill=gold, outline=yemeni_black, width=3)
    draw.ellipse([size - 230, 270, size - 170, 330], fill=gold, outline=yemeni_black, width=3)
    icons_dir = f"{base_dir}/assets/icons"
    images_dir = f"{base_dir}/assets/images"
    img.save(f"{icons_dir}/app_icon.png", "PNG")
    img.save(f"{images_dir}/logo.png", "PNG")
    bg_img = Image.new('RGBA', (size, size), yemeni_green)
    bg_img.paste(img, (0, 0), img)
    bg_img.save(f"{icons_dir}/app_icon_bg.png", "PNG")
    print("OK: Logo generated")
except ImportError:
    print("WARN: Pillow not installed")
    os.system("pip install Pillow")
    print("Please run the script again")
    exit()

print("\nDownloading Arabic fonts...")
fonts_to_download = {
    "Cairo-Regular.ttf": "https://github.com/googlefonts/CairoFont/raw/main/fonts/ttf/Cairo-Regular.ttf",
    "Cairo-Bold.ttf": "https://github.com/googlefonts/CairoFont/raw/main/fonts/ttf/Cairo-Bold.ttf",
    "Cairo-SemiBold.ttf": "https://github.com/googlefonts/CairoFont/raw/main/fonts/ttf/Cairo-SemiBold.ttf",
    "Tajawal-Regular.ttf": "https://github.com/googlefonts/TajawalFont/raw/main/fonts/ttf/Tajawal-Regular.ttf",
    "Tajawal-Bold.ttf": "https://github.com/googlefonts/TajawalFont/raw/main/fonts/ttf/Tajawal-Bold.ttf",
}
fonts_dir = f"{base_dir}/assets/fonts"
for font_name, font_url in fonts_to_download.items():
    font_path = f"{fonts_dir}/{font_name}"
    try:
        print(f"Downloading {font_name}...")
        urllib.request.urlretrieve(font_url, font_path)
        print(f"OK: {font_name}")
    except Exception as e:
        print(f"WARN: Failed to download {font_name}: {e}")

print("\nOK: Fonts downloaded")

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
  fonts:
    - family: Cairo
      fonts:
        - asset: assets/fonts/Cairo-Regular.ttf
        - asset: assets/fonts/Cairo-Bold.ttf
          weight: 700
        - asset: assets/fonts/Cairo-SemiBold.ttf
          weight: 600
    - family: Tajawal
      fonts:
        - asset: assets/fonts/Tajawal-Regular.ttf
        - asset: assets/fonts/Tajawal-Bold.ttf
          weight: 700
""")

write_file(f"{base_dir}/lib/main.dart", """import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_localizations/flutter_localizations.dart';
import 'package:provider/provider.dart';
import 'core/config/routes.dart';
import 'core/config/theme/app_theme.dart';
import 'core/services/local_storage_service.dart';
import 'providers/auth_provider.dart';
import 'providers/law_provider.dart';
import 'providers/consultation_provider.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await SystemChrome.setPreferredOrientations([
    DeviceOrientation.portraitUp,
    DeviceOrientation.portraitDown,
  ]);
  // FIX: Initialize Hive/LocalStorage before running app
  await LocalStorageService.init();
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    // FIX: Wrap with MultiProvider so providers are available throughout the app
    return MultiProvider(
      providers: [
        ChangeNotifierProvider(create: (_) => AuthProvider()),
        ChangeNotifierProvider(create: (_) => LawProvider()),
        ChangeNotifierProvider(create: (_) => ConsultationProvider()),
      ],
      child: MaterialApp.router(
        title: 'Hakki Yamani',
        debugShowCheckedModeBanner: false,
        locale: const Locale('ar', 'YE'),
        localizationsDelegates: const [
          GlobalMaterialLocalizations.delegate,
          GlobalWidgetsLocalizations.delegate,
          GlobalCupertinoLocalizations.delegate,
        ],
        supportedLocales: const [Locale('ar', 'YE'), Locale('ar', 'SA')],
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
      ),
    );
  }
}
""")

write_file(f"{base_dir}/lib/core/config/theme/app_theme.dart", """import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

class AppTheme {
  static const Color yemeniGreen = Color(0xFF1B5E20);
  static const Color yemeniRed = Color(0xFFC62828);
  static const Color yemeniWhite = Color(0xFFFFFFFF);
  static const Color yemeniBlack = Color(0xFF212121);
  static const Color goldAccent = Color(0xFFFFD700);
  static const Color primaryGreen = Color(0xFF2E7D32);
  static const Color lightGreen = Color(0xFF4CAF50);
  static const Color darkGreen = Color(0xFF1B5E20);
  static const Color backgroundLight = Color(0xFFF5F5F5);
  static const Color backgroundDark = Color(0xFF121212);
  static const Color surfaceLight = Color(0xFFFFFFFF);
  static const Color surfaceDark = Color(0xFF1E1E1E);
  static const Color textPrimaryLight = Color(0xFF212121);
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
        surface: surfaceLight,
        error: yemeniRed,
      ),
      appBarTheme: const AppBarTheme(
        backgroundColor: yemeniGreen,
        foregroundColor: yemeniWhite,
        elevation: 0,
        centerTitle: true,
        systemOverlayStyle: SystemUiOverlayStyle.light,
        titleTextStyle: TextStyle(
          fontFamily: 'Cairo',
          fontSize: 20,
          fontWeight: FontWeight.bold,
          color: yemeniWhite,
        ),
      ),
      cardTheme: CardTheme(
        elevation: 2,
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
      ),
      inputDecorationTheme: InputDecorationTheme(
        filled: true,
        fillColor: surfaceLight,
        border: OutlineInputBorder(borderRadius: BorderRadius.circular(12)),
        enabledBorder: OutlineInputBorder(
          borderRadius: BorderRadius.circular(12),
          borderSide: const BorderSide(color: Colors.grey),
        ),
        focusedBorder: OutlineInputBorder(
          borderRadius: BorderRadius.circular(12),
          borderSide: const BorderSide(color: yemeniGreen, width: 2),
        ),
        contentPadding: const EdgeInsets.symmetric(horizontal: 16, vertical: 16),
      ),
      elevatedButtonTheme: ElevatedButtonThemeData(
        style: ElevatedButton.styleFrom(
          backgroundColor: yemeniGreen,
          foregroundColor: yemeniWhite,
          elevation: 2,
          padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 16),
          shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
          textStyle: const TextStyle(fontFamily: 'Cairo', fontSize: 16, fontWeight: FontWeight.bold),
        ),
      ),
      textTheme: const TextTheme(
        displayLarge: TextStyle(fontFamily: 'Cairo', fontSize: 32, fontWeight: FontWeight.bold),
        headlineLarge: TextStyle(fontFamily: 'Cairo', fontSize: 24, fontWeight: FontWeight.bold),
        titleLarge: TextStyle(fontFamily: 'Cairo', fontSize: 20, fontWeight: FontWeight.bold),
        bodyLarge: TextStyle(fontFamily: 'Cairo', fontSize: 16),
        bodyMedium: TextStyle(fontFamily: 'Cairo', fontSize: 14, color: textSecondaryLight),
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
        surface: surfaceDark,
        error: yemeniRed,
      ),
      appBarTheme: const AppBarTheme(
        backgroundColor: darkGreen,
        foregroundColor: yemeniWhite,
        elevation: 0,
        centerTitle: true,
      ),
      cardTheme: CardTheme(
        elevation: 2,
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
      ),
      textTheme: const TextTheme(
        displayLarge: TextStyle(fontFamily: 'Cairo', fontSize: 32, fontWeight: FontWeight.bold, color: textPrimaryDark),
        headlineLarge: TextStyle(fontFamily: 'Cairo', fontSize: 24, fontWeight: FontWeight.bold, color: textPrimaryDark),
        bodyLarge: TextStyle(fontFamily: 'Cairo', fontSize: 16, color: textPrimaryDark),
        bodyMedium: TextStyle(fontFamily: 'Cairo', fontSize: 14, color: textSecondaryDark),
      ),
    );
  }
}
""")

write_file(f"{base_dir}/lib/core/config/routes.dart", """import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import '../../features/auth/screens/login_screen.dart';
import '../../features/auth/screens/register_screen.dart';
import '../../features/auth/screens/otp_screen.dart';
import '../../features/home/screens/home_screen.dart';
import '../../features/laws/screens/laws_list_screen.dart';
import '../../features/laws/screens/law_detail_screen.dart';
import '../../features/laws/screens/search_screen.dart';
import '../../features/consultations/screens/consultations_list_screen.dart';
import '../../features/consultations/screens/consultation_detail_screen.dart';
import '../../features/consultations/screens/new_consultation_screen.dart';
import '../../features/profile/screens/profile_screen.dart';
import '../../features/profile/screens/edit_profile_screen.dart';
import '../../features/lawyer/screens/lawyer_dashboard_screen.dart';
import '../../features/lawyer/screens/lawyer_profile_screen.dart';
import '../../features/about/screens/about_screen.dart';
import '../../features/about/screens/privacy_screen.dart';
import '../../features/about/screens/terms_screen.dart';
import '../../features/faq/screens/faq_screen.dart';

class AppRouter {
  static final GoRouter router = GoRouter(
    initialLocation: '/login',
    routes: [
      GoRoute(path: '/login', name: 'login', builder: (context, state) => const LoginScreen()),
      GoRoute(path: '/register', name: 'register', builder: (context, state) => const RegisterScreen()),
      GoRoute(path: '/otp', name: 'otp', builder: (context, state) => const OtpScreen()),
      GoRoute(path: '/', name: 'home', builder: (context, state) => const HomeScreen()),
      GoRoute(path: '/laws', name: 'laws', builder: (context, state) => const LawsListScreen()),
      GoRoute(path: '/law/:id', name: 'lawDetail', builder: (context, state) => LawDetailScreen(lawId: state.pathParameters['id']!)),
      GoRoute(path: '/search', name: 'search', builder: (context, state) => const SearchScreen()),
      GoRoute(path: '/consultations', name: 'consultations', builder: (context, state) => const ConsultationsListScreen()),
      GoRoute(path: '/consultation/:id', name: 'consultationDetail', builder: (context, state) => ConsultationDetailScreen(consultationId: state.pathParameters['id']!)),
      GoRoute(path: '/new-consultation', name: 'newConsultation', builder: (context, state) => const NewConsultationScreen()),
      GoRoute(path: '/profile', name: 'profile', builder: (context, state) => const ProfileScreen()),
      GoRoute(path: '/edit-profile', name: 'editProfile', builder: (context, state) => const EditProfileScreen()),
      GoRoute(path: '/lawyer-dashboard', name: 'lawyerDashboard', builder: (context, state) => const LawyerDashboardScreen()),
      GoRoute(path: '/lawyer-profile/:id', name: 'lawyerProfile', builder: (context, state) => LawyerProfileScreen(lawyerId: state.pathParameters['id']!)),
      GoRoute(path: '/about', name: 'about', builder: (context, state) => const AboutScreen()),
      GoRoute(path: '/privacy', name: 'privacy', builder: (context, state) => const PrivacyScreen()),
      GoRoute(path: '/terms', name: 'terms', builder: (context, state) => const TermsScreen()),
      GoRoute(path: '/faq', name: 'faq', builder: (context, state) => const FaqScreen()),
    ],
    errorBuilder: (context, state) => Scaffold(
      appBar: AppBar(title: const Text('Error')),
      body: const Center(child: Text('Page not found')),
    ),
  );
}
""")

write_file(f"{base_dir}/lib/core/services/local_storage_service.dart", """import 'package:hive_flutter/hive_flutter.dart';

class LocalStorageService {
  static const String lawsBoxName = 'laws_box';
  static const String userBoxName = 'user_box';
  static const String settingsBoxName = 'settings_box';

  static late Box _lawsBox;
  static late Box _userBox;
  static late Box _settingsBox;

  static Future<void> init() async {
    _lawsBox = await Hive.openBox(lawsBoxName);
    _userBox = await Hive.openBox(userBoxName);
    _settingsBox = await Hive.openBox(settingsBoxName);
  }

  static Future<void> saveLaw(String lawId, Map<String, dynamic> lawData) async {
    await _lawsBox.put(lawId, lawData);
  }

  static Map<String, dynamic>? getLaw(String lawId) {
    return _lawsBox.get(lawId);
  }

  static Future<void> saveUserData(String key, dynamic value) async {
    await _userBox.put(key, value);
  }

  static dynamic getUserData(String key) {
    return _userBox.get(key);
  }

  static Future<void> saveSetting(String key, dynamic value) async {
    await _settingsBox.put(key, value);
  }

  static dynamic getSetting(String key, {dynamic defaultValue}) {
    return _settingsBox.get(key, defaultValue: defaultValue);
  }

  static Future<void> clearAll() async {
    await _lawsBox.clear();
    await _userBox.clear();
    await _settingsBox.clear();
  }
}
""")

write_file(f"{base_dir}/lib/providers/law_provider.dart", """import 'package:flutter/material.dart';
import 'package:cloud_firestore/cloud_firestore.dart';

class LawProvider extends ChangeNotifier {
  final FirebaseFirestore _firestore = FirebaseFirestore.instance;
  List<Map<String, dynamic>> _laws = [];
  bool _isLoading = false;

  List<Map<String, dynamic>> get laws => _laws;
  bool get isLoading => _isLoading;

  Future<void> fetchLaws() async {
    _isLoading = true;
    notifyListeners();
    try {
      final snapshot = await _firestore.collection('laws').get();
      _laws = snapshot.docs.map((doc) => doc.data()).toList();
    } catch (e) {
      print('Error fetching laws: $e');
    }
    _isLoading = false;
    notifyListeners();
  }
}
""")

write_file(f"{base_dir}/lib/providers/consultation_provider.dart", """import 'package:flutter/material.dart';
import 'package:cloud_firestore/cloud_firestore.dart';

class ConsultationProvider extends ChangeNotifier {
  final FirebaseFirestore _firestore = FirebaseFirestore.instance;
  List<Map<String, dynamic>> _consultations = [];
  bool _isLoading = false;

  List<Map<String, dynamic>> get consultations => _consultations;
  bool get isLoading => _isLoading;

  Future<void> fetchMyConsultations(String userId) async {
    _isLoading = true;
    notifyListeners();
    try {
      final snapshot = await _firestore
          .collection('consultations')
          .where('clientId', isEqualTo: userId)
          .orderBy('createdAt', descending: true)
          .get();
      _consultations = snapshot.docs.map((doc) => {'id': doc.id, ...doc.data()}).toList();
    } catch (e) {
      print('Error fetching consultations: $e');
    }
    _isLoading = false;
    notifyListeners();
  }

  Future<String> createConsultation(Map<String, dynamic> data) async {
    try {
      final docRef = await _firestore.collection('consultations').add({
        ...data,
        'createdAt': FieldValue.serverTimestamp(),
        'status': 'pending',
      });
      notifyListeners();
      return docRef.id;
    } catch (e) {
      throw Exception('Failed to create consultation');
    }
  }
}
""")

write_file(f"{base_dir}/lib/features/auth/screens/login_screen.dart", """import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import '../../../core/config/theme/app_theme.dart';

class LoginScreen extends StatefulWidget {
  const LoginScreen({super.key});
  @override
  State<LoginScreen> createState() => _LoginScreenState();
}

class _LoginScreenState extends State<LoginScreen> {
  final _formKey = GlobalKey<FormState>();
  final _emailController = TextEditingController();
  final _passwordController = TextEditingController();
  bool _obscurePassword = true;

  @override
  void dispose() {
    _emailController.dispose();
    _passwordController.dispose();
    super.dispose();
  }

  Future<void> _handleLogin() async {
    if (!_formKey.currentState!.validate()) return;
    if (mounted) {
      context.go('/');
    }
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
              const Text('Hakki Yamani', textAlign: TextAlign.center, style: TextStyle(fontFamily: 'Cairo', fontSize: 32, fontWeight: FontWeight.bold, color: AppTheme.yemeniGreen)),
              const SizedBox(height: 8),
              const Text('Login', textAlign: TextAlign.center, style: TextStyle(fontFamily: 'Cairo', fontSize: 18, color: AppTheme.textSecondaryLight)),
              const SizedBox(height: 48),
              Form(
                key: _formKey,
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.stretch,
                  children: [
                    TextFormField(controller: _emailController, keyboardType: TextInputType.emailAddress, decoration: const InputDecoration(labelText: 'Email', prefixIcon: Icon(Icons.email_outlined)), validator: (value) {
                      if (value == null || value.isEmpty) return 'Enter email';
                      if (!value.contains('@')) return 'Invalid email';
                      return null;
                    }),
                    const SizedBox(height: 16),
                    TextFormField(controller: _passwordController, obscureText: _obscurePassword, decoration: InputDecoration(labelText: 'Password', prefixIcon: const Icon(Icons.lock_outlined), suffixIcon: IconButton(icon: Icon(_obscurePassword ? Icons.visibility_outlined : Icons.visibility_off_outlined), onPressed: () => setState(() => _obscurePassword = !_obscurePassword))), validator: (value) {
                      if (value == null || value.isEmpty) return 'Enter password';
                      return null;
                    }),
                    const SizedBox(height: 24),
                    ElevatedButton(onPressed: _handleLogin, child: const Text('Login')),
                    const SizedBox(height: 24),
                    const Row(children: [Expanded(child: Divider()), Padding(padding: EdgeInsets.symmetric(horizontal: 16), child: Text('OR')), Expanded(child: Divider())]),
                    const SizedBox(height: 24),
                    OutlinedButton.icon(onPressed: () => context.push('/otp'), icon: const Icon(Icons.phone_android), label: const Text('Login with Phone'), style: OutlinedButton.styleFrom(padding: const EdgeInsets.symmetric(vertical: 16))),
                    const SizedBox(height: 24),
                    Row(mainAxisAlignment: MainAxisAlignment.center, children: [const Text("Don't have account?"), TextButton(onPressed: () => context.push('/register'), child: const Text('Register', style: TextStyle(fontWeight: FontWeight.bold)))]),
                  ],
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
""")

write_file(f"{base_dir}/lib/features/auth/screens/register_screen.dart", """import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import '../../../core/config/theme/app_theme.dart';

class RegisterScreen extends StatefulWidget {
  const RegisterScreen({super.key});
  @override
  State<RegisterScreen> createState() => _RegisterScreenState();
}

class _RegisterScreenState extends State<RegisterScreen> {
  final _formKey = GlobalKey<FormState>();
  final _fullNameController = TextEditingController();
  final _emailController = TextEditingController();
  final _phoneController = TextEditingController();
  final _passwordController = TextEditingController();
  final _confirmPasswordController = TextEditingController();
  bool _obscurePassword = true;
  bool _obscureConfirmPassword = true;
  String _userType = 'citizen';

  @override
  void dispose() {
    _fullNameController.dispose();
    _emailController.dispose();
    _phoneController.dispose();
    _passwordController.dispose();
    _confirmPasswordController.dispose();
    super.dispose();
  }

  Future<void> _handleRegister() async {
    if (!_formKey.currentState!.validate()) return;
    if (_passwordController.text != _confirmPasswordController.text) {
      ScaffoldMessenger.of(context).showSnackBar(const SnackBar(content: Text('Passwords do not match'), backgroundColor: AppTheme.yemeniRed));
      return;
    }
    if (mounted) {
      ScaffoldMessenger.of(context).showSnackBar(const SnackBar(content: Text('Account created'), backgroundColor: AppTheme.yemeniGreen));
      context.go('/');
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Register'), leading: IconButton(icon: const Icon(Icons.arrow_back), onPressed: () => context.pop())),
      body: SafeArea(
        child: SingleChildScrollView(
          padding: const EdgeInsets.all(24),
          child: Form(
            key: _formKey,
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.stretch,
              children: [
                const Icon(Icons.person_add, size: 80, color: AppTheme.yemeniGreen),
                const SizedBox(height: 24),
                const Text('Join Now', textAlign: TextAlign.center, style: TextStyle(fontFamily: 'Cairo', fontSize: 24, fontWeight: FontWeight.bold)),
                const SizedBox(height: 32),
                TextFormField(controller: _fullNameController, decoration: const InputDecoration(labelText: 'Full Name', prefixIcon: Icon(Icons.person_outline)), validator: (value) => value == null || value.isEmpty ? 'Enter name' : null),
                const SizedBox(height: 16),
                TextFormField(controller: _emailController, keyboardType: TextInputType.emailAddress, decoration: const InputDecoration(labelText: 'Email', prefixIcon: Icon(Icons.email_outlined)), validator: (value) {
                  if (value == null || value.isEmpty) return 'Enter email';
                  if (!value.contains('@')) return 'Invalid email';
                  return null;
                }),
                const SizedBox(height: 16),
                TextFormField(controller: _phoneController, keyboardType: TextInputType.phone, decoration: const InputDecoration(labelText: 'Phone', prefixIcon: Icon(Icons.phone_outlined), hintText: '+967xxxxxxxxx'), validator: (value) => value == null || value.isEmpty ? 'Enter phone' : null),
                const SizedBox(height: 16),
                TextFormField(controller: _passwordController, obscureText: _obscurePassword, decoration: InputDecoration(labelText: 'Password', prefixIcon: const Icon(Icons.lock_outlined), suffixIcon: IconButton(icon: Icon(_obscurePassword ? Icons.visibility_outlined : Icons.visibility_off_outlined), onPressed: () => setState(() => _obscurePassword = !_obscurePassword))), validator: (value) {
                  if (value == null || value.isEmpty) return 'Enter password';
                  if (value.length < 6) return 'Min 6 characters';
                  return null;
                }),
                const SizedBox(height: 16),
                TextFormField(controller: _confirmPasswordController, obscureText: _obscureConfirmPassword, decoration: InputDecoration(labelText: 'Confirm Password', prefixIcon: const Icon(Icons.lock_outlined), suffixIcon: IconButton(icon: Icon(_obscureConfirmPassword ? Icons.visibility_outlined : Icons.visibility_off_outlined), onPressed: () => setState(() => _obscureConfirmPassword = !_obscureConfirmPassword))), validator: (value) => value == null || value.isEmpty ? 'Confirm password' : null),
                const SizedBox(height: 24),
                const Text('Account Type', style: TextStyle(fontFamily: 'Cairo', fontSize: 16, fontWeight: FontWeight.bold)),
                const SizedBox(height: 12),
                Row(children: [
                  Expanded(child: RadioListTile<String>(title: const Text('Citizen'), value: 'citizen', groupValue: _userType, onChanged: (value) => setState(() => _userType = value!))),
                  Expanded(child: RadioListTile<String>(title: const Text('Lawyer'), value: 'lawyer', groupValue: _userType, onChanged: (value) => setState(() => _userType = value!))),
                ]),
                const SizedBox(height: 24),
                ElevatedButton(onPressed: _handleRegister, child: const Text('Create Account')),
                const SizedBox(height: 16),
                Row(mainAxisAlignment: MainAxisAlignment.center, children: [const Text('Have account?'), TextButton(onPressed: () => context.pop(), child: const Text('Login', style: TextStyle(fontWeight: FontWeight.bold)))]),
              ],
            ),
          ),
        ),
      ),
    );
  }
}
""")

write_file(f"{base_dir}/lib/features/auth/screens/otp_screen.dart", """import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import 'package:pin_code_fields/pin_code_fields.dart';
import '../../../core/config/theme/app_theme.dart';

class OtpScreen extends StatefulWidget {
  const OtpScreen({super.key});
  @override
  State<OtpScreen> createState() => _OtpScreenState();
}

class _OtpScreenState extends State<OtpScreen> {
  final _phoneController = TextEditingController();
  String _currentCode = '';
  bool _isCodeSent = false;

  @override
  void dispose() {
    _phoneController.dispose();
    super.dispose();
  }

  Future<void> _sendOtp() async {
    if (_phoneController.text.isEmpty) {
      ScaffoldMessenger.of(context).showSnackBar(const SnackBar(content: Text('Enter phone'), backgroundColor: AppTheme.yemeniRed));
      return;
    }
    if (mounted) setState(() => _isCodeSent = true);
  }

  Future<void> _verifyOtp() async {
    if (mounted) {
      context.go('/');
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Verify Phone'), leading: IconButton(icon: const Icon(Icons.arrow_back), onPressed: () => context.pop())),
      body: SafeArea(
        child: Padding(
          padding: const EdgeInsets.all(24),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: [
              const SizedBox(height: 40),
              Icon(Icons.phone_android, size: 80, color: AppTheme.yemeniGreen),
              const SizedBox(height: 24),
              const Text('Verify Phone', textAlign: TextAlign.center, style: TextStyle(fontFamily: 'Cairo', fontSize: 24, fontWeight: FontWeight.bold)),
              const SizedBox(height: 16),
              Text(_isCodeSent ? 'Enter code sent to ${_phoneController.text}' : 'Enter your phone', textAlign: TextAlign.center, style: const TextStyle(fontFamily: 'Cairo', fontSize: 16, color: AppTheme.textSecondaryLight)),
              const SizedBox(height: 40),
              if (!_isCodeSent) ...[
                TextField(controller: _phoneController, keyboardType: TextInputType.phone, textAlign: TextAlign.center, decoration: const InputDecoration(labelText: 'Phone', hintText: 'xxxxxxxxx', prefixText: '+967 ')),
                const SizedBox(height: 24),
                ElevatedButton(onPressed: _sendOtp, child: const Text('Send Code')),
              ] else ...[
                PinCodeTextField(appContext: context, length: 6, obscureText: false, animationType: AnimationType.fade, keyboardType: TextInputType.number, pinTheme: PinTheme(shape: PinCodeFieldShape.box, borderRadius: BorderRadius.circular(12), fieldHeight: 60, fieldWidth: 50, activeFillColor: Colors.white, inactiveFillColor: Colors.grey.shade100, selectedFillColor: Colors.white, activeColor: AppTheme.yemeniGreen, inactiveColor: Colors.grey, selectedColor: AppTheme.yemeniGreen), animationDuration: const Duration(milliseconds: 300), backgroundColor: Colors.transparent, enableActiveFill: true, onChanged: (value) => setState(() => _currentCode = value)),
                const SizedBox(height: 32),
                ElevatedButton(onPressed: _verifyOtp, child: const Text('Verify')),
                const SizedBox(height: 16),
                TextButton(onPressed: () => setState(() => _isCodeSent = false), child: const Text('Change Phone')),
              ],
            ],
          ),
        ),
      ),
    );
  }
}
""")

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
    return Scaffold(body: _screens[_selectedIndex], bottomNavigationBar: NavigationBar(
      selectedIndex: _selectedIndex,
      onDestinationSelected: (index) => setState(() => _selectedIndex = index),
      destinations: const [
        NavigationDestination(icon: Icon(Icons.home_outlined), selectedIcon: Icon(Icons.home), label: 'Home'),
        NavigationDestination(icon: Icon(Icons.library_books_outlined), selectedIcon: Icon(Icons.library_books), label: 'Laws'),
        NavigationDestination(icon: Icon(Icons.chat_outlined), selectedIcon: Icon(Icons.chat), label: 'Consult'),
        NavigationDestination(icon: Icon(Icons.person_outline), selectedIcon: Icon(Icons.person), label: 'Profile'),
      ],
    ));
  }
}

class HomeTab extends StatelessWidget {
  const HomeTab({super.key});
  @override
  Widget build(BuildContext context) {
    return CustomScrollView(slivers: [
      SliverAppBar(floating: true, title: const Text('Hakki Yamani'), actions: [IconButton(icon: const Icon(Icons.search), onPressed: () => context.push('/search')), IconButton(icon: const Icon(Icons.notifications_outlined), onPressed: () {})]),
      SliverToBoxAdapter(child: Container(decoration: const BoxDecoration(gradient: LinearGradient(colors: [AppTheme.yemeniGreen, AppTheme.lightGreen], begin: Alignment.topRight, end: Alignment.bottomLeft)), padding: const EdgeInsets.all(24), child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
        const Text('Welcome', style: TextStyle(color: Colors.white, fontSize: 24, fontWeight: FontWeight.bold)),
        const SizedBox(height: 8),
        const Text('Your Legal Encyclopedia', style: TextStyle(color: Colors.white70, fontSize: 16)),
        const SizedBox(height: 16),
        Row(children: [
          Expanded(child: ElevatedButton.icon(onPressed: () => context.push('/laws'), icon: const Icon(Icons.search), label: const Text('Search Laws'), style: ElevatedButton.styleFrom(backgroundColor: Colors.white, foregroundColor: AppTheme.yemeniGreen))),
          const SizedBox(width: 12),
          ElevatedButton.icon(onPressed: () => context.push('/new-consultation'), icon: const Icon(Icons.add), label: const Text('Consult')),
        ]),
      ]))),
      SliverPadding(padding: const EdgeInsets.all(16), sliver: SliverGrid(gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(crossAxisCount: 2, childAspectRatio: 1.2, crossAxisSpacing: 12, mainAxisSpacing: 12), delegate: SliverChildBuilderDelegate((context, index) {
        final items = [{'icon': Icons.gavel, 'title': 'Constitution'}, {'icon': Icons.work, 'title': 'Labor Law'}, {'icon': Icons.family_restroom, 'title': 'Personal Status'}, {'icon': Icons.school, 'title': 'Education'}];
        final item = items[index];
        return Card(child: InkWell(onTap: () => context.push('/laws'), borderRadius: BorderRadius.circular(12), child: Column(mainAxisAlignment: MainAxisAlignment.center, children: [Icon(item['icon'] as IconData, size: 40, color: AppTheme.yemeniGreen), const SizedBox(height: 8), Text(item['title'] as String, style: const TextStyle(fontFamily: 'Cairo', fontWeight: FontWeight.bold), textAlign: TextAlign.center)])));
      }, childCount: 4)))),
      SliverToBoxAdapter(child: Padding(padding: const EdgeInsets.symmetric(horizontal: 16), child: Row(mainAxisAlignment: MainAxisAlignment.spaceBetween, children: [const Text('Latest Laws', style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold)), TextButton(onPressed: () => context.push('/laws'), child: const Text('View All'))]))),
      SliverList(delegate: SliverChildBuilderDelegate((context, index) => Card(margin: const EdgeInsets.symmetric(horizontal: 16, vertical: 8), child: ListTile(leading: CircleAvatar(backgroundColor: AppTheme.yemeniGreen.withOpacity(0.1), child: const Icon(Icons.article, color: AppTheme.yemeniGreen)), title: const Text('Yemen Labor Law'), subtitle: const Text('Last update: 2024'), trailing: const Icon(Icons.arrow_forward_ios, size: 16), onTap: () => context.push('/law/1'))), childCount: 3)),
      const SliverToBoxAdapter(child: SizedBox(height: 16)),
    ]);
  }
}

class LawsTab extends StatelessWidget {
  const LawsTab({super.key});
  @override
  Widget build(BuildContext context) => const Center(child: Text('Laws', style: TextStyle(fontSize: 20)));
}

class ConsultationsTab extends StatelessWidget {
  const ConsultationsTab({super.key});
  @override
  Widget build(BuildContext context) => const Center(child: Text('Consultations', style: TextStyle(fontSize: 20)));
}

class ProfileTab extends StatelessWidget {
  const ProfileTab({super.key});
  @override
  Widget build(BuildContext context) => const Center(child: Text('Profile', style: TextStyle(fontSize: 20)));
}
""")

write_file(f"{base_dir}/lib/features/laws/screens/laws_list_screen.dart", """import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import '../../../core/config/theme/app_theme.dart';

class LawsListScreen extends StatefulWidget {
  const LawsListScreen({super.key});
  @override
  State<LawsListScreen> createState() => _LawsListScreenState();
}

class _LawsListScreenState extends State<LawsListScreen> {
  String _selectedCategory = 'all';
  final List<Map<String, dynamic>> _categories = [
    {'id': 'all', 'name': 'All', 'icon': Icons.library_books},
    {'id': 'constitution', 'name': 'Constitution', 'icon': Icons.gavel},
    {'id': 'labor', 'name': 'Labor', 'icon': Icons.work},
    {'id': 'personal_status', 'name': 'Personal', 'icon': Icons.family_restroom},
    {'id': 'education', 'name': 'Education', 'icon': Icons.school},
  ];
  final List<Map<String, dynamic>> _laws = [
    {'id': '1', 'title': 'Yemen Constitution', 'category': 'constitution', 'articlesCount': 150, 'lastUpdate': '2024-01-15'},
    {'id': '2', 'title': 'Labor Law', 'category': 'labor', 'articlesCount': 200, 'lastUpdate': '2024-02-20'},
    {'id': '3', 'title': 'Personal Status', 'category': 'personal_status', 'articlesCount': 180, 'lastUpdate': '2024-01-10'},
    {'id': '4', 'title': 'Education Law', 'category': 'education', 'articlesCount': 120, 'lastUpdate': '2024-03-05'},
  ];
  List<Map<String, dynamic>> get _filteredLaws => _selectedCategory == 'all' ? _laws : _laws.where((law) => law['category'] == _selectedCategory).toList();

  @override
  Widget build(BuildContext context) {
    return Scaffold(appBar: AppBar(title: const Text('Legal Encyclopedia'), actions: [IconButton(icon: const Icon(Icons.search), onPressed: () => context.push('/search'))]), body: Column(children: [
      SizedBox(height: 100, child: ListView.builder(scrollDirection: Axis.horizontal, padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 8), itemCount: _categories.length, itemBuilder: (context, index) {
        final category = _categories[index];
        final isSelected = _selectedCategory == category['id'];
        return Padding(padding: const EdgeInsets.only(left: 8), child: FilterChip(label: Row(mainAxisSize: MainAxisSize.min, children: [Icon(category['icon'], size: 18), const SizedBox(width: 8), Text(category['name'])]), selected: isSelected, onSelected: (selected) => setState(() => _selectedCategory = category['id']), backgroundColor: Colors.grey.shade100, selectedColor: AppTheme.yemeniGreen.withOpacity(0.2)));
      })),
      const Divider(),
      Expanded(child: ListView.builder(padding: const EdgeInsets.all(16), itemCount: _filteredLaws.length, itemBuilder: (context, index) {
        final law = _filteredLaws[index];
        return Card(margin: const EdgeInsets.only(bottom: 12), child: ListTile(leading: CircleAvatar(backgroundColor: AppTheme.yemeniGreen.withOpacity(0.1), child: const Icon(Icons.article, color: AppTheme.yemeniGreen)), title: Text(law['title'], style: const TextStyle(fontFamily: 'Cairo', fontWeight: FontWeight.bold)), subtitle: Text('${law['articlesCount']} articles - ${law['lastUpdate']}'), trailing: const Icon(Icons.arrow_forward_ios, size: 16), onTap: () => context.push('/law/${law['id']}')));
      })),
    ]));
  }
}
""")

write_file(f"{base_dir}/lib/features/laws/screens/search_screen.dart", """import 'package:flutter/material.dart';

class SearchScreen extends StatefulWidget {
  const SearchScreen({super.key});
  @override
  State<SearchScreen> createState() => _SearchScreenState();
}

class _SearchScreenState extends State<SearchScreen> {
  final _searchController = TextEditingController();
  List<Map<String, dynamic>> _searchResults = [];
  bool _isSearching = false;
  final List<Map<String, dynamic>> _allLaws = [
    {'id': '1', 'title': 'Yemen Constitution', 'category': 'Constitution'},
    {'id': '2', 'title': 'Labor Law', 'category': 'Labor'},
    {'id': '3', 'title': 'Personal Status', 'category': 'Personal'},
  ];

  void _search(String query) {
    if (query.isEmpty) {
      setState(() => _searchResults = []);
      return;
    }
    setState(() => _isSearching = true);
    Future.delayed(const Duration(milliseconds: 500), () {
      setState(() {
        _searchResults = _allLaws.where((law) => law['title'].contains(query) || law['category'].contains(query)).toList();
        _isSearching = false;
      });
    });
  }

  @override
  void dispose() {
    _searchController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(appBar: AppBar(title: const Text('Search Laws')), body: Column(children: [
      Padding(padding: const EdgeInsets.all(16), child: TextField(controller: _searchController, decoration: InputDecoration(hintText: 'Search...', prefixIcon: const Icon(Icons.search), suffixIcon: _searchController.text.isNotEmpty ? IconButton(icon: const Icon(Icons.clear), onPressed: () { _searchController.clear(); _search(''); }) : null, border: OutlineInputBorder(borderRadius: BorderRadius.circular(12))), onChanged: _search)),
      if (_isSearching) const Expanded(child: Center(child: CircularProgressIndicator()))
      else if (_searchResults.isEmpty && _searchController.text.isNotEmpty)
        Expanded(child: Center(child: Column(mainAxisAlignment: MainAxisAlignment.center, children: [Icon(Icons.search_off, size: 80, color: Colors.grey.shade400), const SizedBox(height: 16), const Text('No results', style: TextStyle(fontSize: 18, color: Colors.grey))])))
      else
        Expanded(child: ListView.builder(padding: const EdgeInsets.symmetric(horizontal: 16), itemCount: _searchResults.length, itemBuilder: (context, index) {
          final result = _searchResults[index];
          return Card(margin: const EdgeInsets.only(bottom: 8), child: ListTile(leading: const Icon(Icons.article), title: Text(result['title']), subtitle: Text(result['category']), onTap: () {}));
        })),
    ]));
  }
}
""")

write_file(f"{base_dir}/lib/features/consultations/screens/consultations_list_screen.dart", """import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import '../../../core/config/theme/app_theme.dart';

class ConsultationsListScreen extends StatefulWidget {
  const ConsultationsListScreen({super.key});
  @override
  State<ConsultationsListScreen> createState() => _ConsultationsListScreenState();
}

class _ConsultationsListScreenState extends State<ConsultationsListScreen> with SingleTickerProviderStateMixin {
  late TabController _tabController;
  final List<Map<String, dynamic>> _consultations = [
    {'id': '1', 'title': 'Work Contract', 'lawyerName': 'Ahmed Ali', 'status': 'in_progress', 'date': '2024-06-25', 'lastMessage': 'I will review'},
    {'id': '2', 'title': 'Divorce Case', 'lawyerName': 'Fatima Ahmed', 'status': 'completed', 'date': '2024-06-20', 'lastMessage': 'Completed'},
  ];

  @override
  void initState() {
    super.initState();
    _tabController = TabController(length: 3, vsync: this);
  }

  @override
  void dispose() {
    _tabController.dispose();
    super.dispose();
  }

  Color _getStatusColor(String status) {
    switch (status) {
      case 'pending': return Colors.orange;
      case 'in_progress': return Colors.blue;
      case 'completed': return Colors.green;
      case 'cancelled': return Colors.red;
      default: return Colors.grey;
    }
  }

  String _getStatusText(String status) {
    switch (status) {
      case 'pending': return 'Pending';
      case 'in_progress': return 'In Progress';
      case 'completed': return 'Completed';
      case 'cancelled': return 'Cancelled';
      default: return status;
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(appBar: AppBar(title: const Text('My Consultations'), bottom: TabBar(controller: _tabController, tabs: const [Tab(text: 'All'), Tab(text: 'In Progress'), Tab(text: 'Completed')])), body: TabBarView(controller: _tabController, children: [_buildList(_consultations), _buildList(_consultations.where((c) => c['status'] == 'in_progress').toList()), _buildList(_consultations.where((c) => c['status'] == 'completed').toList())]), floatingActionButton: FloatingActionButton.extended(onPressed: () => context.push('/new-consultation'), icon: const Icon(Icons.add), label: const Text('New')));
  }

  Widget _buildList(List<Map<String, dynamic>> consultations) {
    if (consultations.isEmpty) return const Center(child: Column(mainAxisAlignment: MainAxisAlignment.center, children: [Icon(Icons.chat_bubble_outline, size: 80, color: Colors.grey), SizedBox(height: 16), Text('No consultations', style: TextStyle(fontSize: 18, color: Colors.grey))]));
    return ListView.builder(padding: const EdgeInsets.all(16), itemCount: consultations.length, itemBuilder: (context, index) {
      final c = consultations[index];
      return Card(margin: const EdgeInsets.only(bottom: 12), child: ListTile(leading: CircleAvatar(backgroundColor: AppTheme.yemeniGreen.withOpacity(0.1), child: const Icon(Icons.person, color: AppTheme.yemeniGreen)), title: Text(c['title'], style: const TextStyle(fontWeight: FontWeight.bold)), subtitle: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [const SizedBox(height: 4), Text(c['lawyerName']), const SizedBox(height: 4), Text(c['lastMessage'], maxLines: 1, overflow: TextOverflow.ellipsis)]), trailing: Column(mainAxisAlignment: MainAxisAlignment.center, crossAxisAlignment: CrossAxisAlignment.end, children: [Container(padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 4), decoration: BoxDecoration(color: _getStatusColor(c['status']).withOpacity(0.1), borderRadius: BorderRadius.circular(12)), child: Text(_getStatusText(c['status']), style: TextStyle(color: _getStatusColor(c['status']), fontSize: 12, fontWeight: FontWeight.bold))), const SizedBox(height: 4), Text(c['date'], style: TextStyle(fontSize: 12, color: Colors.grey.shade600))]), onTap: () => context.push('/consultation/${c['id']}')));
    });
  }
}
""")

write_file(f"{base_dir}/lib/features/consultations/screens/new_consultation_screen.dart", """import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';

class NewConsultationScreen extends StatefulWidget {
  const NewConsultationScreen({super.key});
  @override
  State<NewConsultationScreen> createState() => _NewConsultationScreenState();
}

class _NewConsultationScreenState extends State<NewConsultationScreen> {
  final _formKey = GlobalKey<FormState>();
  final _titleController = TextEditingController();
  final _descriptionController = TextEditingController();
  String _selectedCategory = '';
  final List<String> _categories = ['Labor Law', 'Personal Status', 'Criminal', 'Civil', 'Education', 'Other'];

  @override
  void dispose() {
    _titleController.dispose();
    _descriptionController.dispose();
    super.dispose();
  }

  void _submitConsultation() {
    if (!_formKey.currentState!.validate()) return;
    showDialog(context: context, builder: (context) => AlertDialog(title: const Text('Sent'), content: const Text('Your consultation has been sent'), actions: [TextButton(onPressed: () { Navigator.pop(context); context.pop(); }, child: const Text('OK'))]));
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(appBar: AppBar(title: const Text('New Consultation')), body: SingleChildScrollView(padding: const EdgeInsets.all(24), child: Form(key: _formKey, child: Column(crossAxisAlignment: CrossAxisAlignment.stretch, children: [
      TextFormField(controller: _titleController, decoration: const InputDecoration(labelText: 'Title', hintText: 'e.g. Work contract question'), validator: (value) => value == null || value.isEmpty ? 'Enter title' : null),
      const SizedBox(height: 16),
      DropdownButtonFormField<String>(decoration: const InputDecoration(labelText: 'Category'), value: _selectedCategory.isEmpty ? null : _selectedCategory, items: _categories.map((category) => DropdownMenuItem(value: category, child: Text(category))).toList(), onChanged: (value) => setState(() => _selectedCategory = value!), validator: (value) => value == null || value.isEmpty ? 'Select category' : null),
      const SizedBox(height: 16),
      TextFormField(controller: _descriptionController, decoration: const InputDecoration(labelText: 'Details', hintText: 'Explain your question...'), maxLines: 6, validator: (value) => value == null || value.isEmpty ? 'Enter details' : null),
      const SizedBox(height: 24),
      Card(child: ListTile(leading: const Icon(Icons.attach_file), title: const Text('Attach Files'), subtitle: const Text('PDF, Images'), trailing: const Icon(Icons.arrow_forward_ios, size: 16), onTap: () {})),
      const SizedBox(height: 24),
      ElevatedButton.icon(onPressed: _submitConsultation, icon: const Icon(Icons.send), label: const Text('Send'), style: ElevatedButton.styleFrom(padding: const EdgeInsets.symmetric(vertical: 16))),
    ]))));
  }
}
""")

write_file(f"{base_dir}/lib/features/profile/screens/profile_screen.dart", """import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import '../../../core/config/theme/app_theme.dart';

class ProfileScreen extends StatelessWidget {
  const ProfileScreen({super.key});
  @override
  Widget build(BuildContext context) {
    return Scaffold(appBar: AppBar(title: const Text('Profile'), actions: [IconButton(icon: const Icon(Icons.settings), onPressed: () {})]), body: SingleChildScrollView(child: Column(children: [
      const SizedBox(height: 24),
      CircleAvatar(radius: 60, backgroundColor: AppTheme.yemeniGreen.withOpacity(0.1), child: const Icon(Icons.person, size: 60, color: AppTheme.yemeniGreen)),
      const SizedBox(height: 16),
      const Text('User', textAlign: TextAlign.center, style: TextStyle(fontFamily: 'Cairo', fontSize: 24, fontWeight: FontWeight.bold)),
      Text('Citizen', style: TextStyle(color: Colors.grey.shade600)),
      const SizedBox(height: 24),
      _buildMenuItem(context, icon: Icons.person_outline, title: 'Edit Profile', onTap: () => context.push('/edit-profile')),
      _buildMenuItem(context, icon: Icons.chat_bubble_outline, title: 'Consultations', onTap: () => context.push('/consultations')),
      _buildMenuItem(context, icon: Icons.bookmark_border, title: 'Saved', onTap: () {}),
      _buildMenuItem(context, icon: Icons.help_outline, title: 'FAQ', onTap: () => context.push('/faq')),
      _buildMenuItem(context, icon: Icons.info_outline, title: 'About', onTap: () => context.push('/about')),
      _buildMenuItem(context, icon: Icons.privacy_tip_outlined, title: 'Privacy', onTap: () => context.push('/privacy')),
      const Divider(height: 32),
      ListTile(leading: const Icon(Icons.logout, color: AppTheme.yemeniRed), title: const Text('Logout', style: TextStyle(color: AppTheme.yemeniRed)), onTap: () => context.go('/login')),
      const SizedBox(height: 24),
    ])));
  }

  Widget _buildMenuItem(BuildContext context, {required IconData icon, required String title, required VoidCallback onTap}) {
    return Card(margin: const EdgeInsets.symmetric(horizontal: 16, vertical: 4), child: ListTile(leading: Icon(icon, color: AppTheme.yemeniGreen), title: Text(title, style: const TextStyle(fontFamily: 'Cairo')), trailing: const Icon(Icons.arrow_forward_ios, size: 16), onTap: onTap));
  }
}
""")

write_file(f"{base_dir}/lib/features/profile/screens/edit_profile_screen.dart", """import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import '../../../core/config/theme/app_theme.dart';

class EditProfileScreen extends StatefulWidget {
  const EditProfileScreen({super.key});
  @override
  State<EditProfileScreen> createState() => _EditProfileScreenState();
}

class _EditProfileScreenState extends State<EditProfileScreen> {
  final _formKey = GlobalKey<FormState>();
  final _fullNameController = TextEditingController();
  final _emailController = TextEditingController();
  final _phoneController = TextEditingController();

  @override
  void dispose() {
    _fullNameController.dispose();
    _emailController.dispose();
    _phoneController.dispose();
    super.dispose();
  }

  Future<void> _saveProfile() async {
    if (!_formKey.currentState!.validate()) return;
    if (mounted) {
      ScaffoldMessenger.of(context).showSnackBar(const SnackBar(content: Text('Saved'), backgroundColor: AppTheme.yemeniGreen));
      context.pop();
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(appBar: AppBar(title: const Text('Edit Profile')), body: SingleChildScrollView(padding: const EdgeInsets.all(24), child: Form(key: _formKey, child: Column(children: [
      Stack(children: [
        CircleAvatar(radius: 60, backgroundColor: AppTheme.yemeniGreen.withOpacity(0.1), child: const Icon(Icons.person, size: 60, color: AppTheme.yemeniGreen)),
        Positioned(bottom: 0, right: 0, child: CircleAvatar(backgroundColor: AppTheme.yemeniGreen, child: IconButton(icon: const Icon(Icons.camera_alt, color: Colors.white, size: 20), onPressed: () {}))),
      ]),
      const SizedBox(height: 32),
      TextFormField(controller: _fullNameController, decoration: const InputDecoration(labelText: 'Full Name', prefixIcon: Icon(Icons.person_outline)), validator: (value) => value == null || value.isEmpty ? 'Enter name' : null),
      const SizedBox(height: 16),
      TextFormField(controller: _emailController, decoration: const InputDecoration(labelText: 'Email', prefixIcon: Icon(Icons.email_outlined)), enabled: false),
      const SizedBox(height: 16),
      TextFormField(controller: _phoneController, decoration: const InputDecoration(labelText: 'Phone', prefixIcon: Icon(Icons.phone_outlined)), validator: (value) => value == null || value.isEmpty ? 'Enter phone' : null),
      const SizedBox(height: 32),
      ElevatedButton.icon(onPressed: _saveProfile, icon: const Icon(Icons.save), label: const Text('Save'), style: ElevatedButton.styleFrom(padding: const EdgeInsets.symmetric(horizontal: 48, vertical: 16))),
    ]))));
  }
}
""")

write_file(f"{base_dir}/lib/features/lawyer/screens/lawyer_dashboard_screen.dart", """import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import '../../../core/config/theme/app_theme.dart';

class LawyerDashboardScreen extends StatefulWidget {
  const LawyerDashboardScreen({super.key});
  @override
  State<LawyerDashboardScreen> createState() => _LawyerDashboardScreenState();
}

class _LawyerDashboardScreenState extends State<LawyerDashboardScreen> {
  final List<Map<String, dynamic>> _pendingRequests = [
    {'id': '1', 'clientName': 'Mohammed', 'title': 'Work question', 'date': '5 min ago'},
    {'id': '2', 'clientName': 'Sara', 'title': 'Custody case', 'date': '1 hour ago'},
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(appBar: AppBar(title: const Text('Lawyer Dashboard')), body: SingleChildScrollView(padding: const EdgeInsets.all(16), child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
      Row(children: [
        Expanded(child: _buildStatCard('New', '12', Icons.pending_actions, Colors.orange)),
        const SizedBox(width: 12),
        Expanded(child: _buildStatCard('In Progress', '5', Icons.hourglass_bottom, Colors.blue)),
        const SizedBox(width: 12),
        Expanded(child: _buildStatCard('Completed', '48', Icons.check_circle, Colors.green)),
      ]),
      const SizedBox(height: 24),
      const Text('Pending Requests', style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold)),
      const SizedBox(height: 12),
      ListView.builder(shrinkWrap: true, physics: const NeverScrollableScrollPhysics(), itemCount: _pendingRequests.length, itemBuilder: (context, index) {
        final req = _pendingRequests[index];
        return Card(margin: const EdgeInsets.only(bottom: 12), child: Padding(padding: const EdgeInsets.all(16), child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
          Row(mainAxisAlignment: MainAxisAlignment.spaceBetween, children: [Text(req['clientName'], style: const TextStyle(fontWeight: FontWeight.bold, fontSize: 16)), Text(req['date'], style: TextStyle(color: Colors.grey.shade600, fontSize: 12))]),
          const SizedBox(height: 8),
          Text(req['title']),
          const SizedBox(height: 16),
          Row(children: [Expanded(child: OutlinedButton(onPressed: () {}, child: const Text('Reject'))), const SizedBox(width: 12), Expanded(child: ElevatedButton(onPressed: () => context.push('/consultation/${req['id']}'), child: const Text('Accept')))]),
        ])));
      }),
    ])));
  }

  Widget _buildStatCard(String title, String value, IconData icon, Color color) {
    return Card(child: Padding(padding: const EdgeInsets.all(16), child: Column(children: [Icon(icon, color: color, size: 30), const SizedBox(height: 8), Text(value, style: const TextStyle(fontSize: 20, fontWeight: FontWeight.bold)), Text(title, style: const TextStyle(fontSize: 12), textAlign: TextAlign.center)])));
  }
}
""")

write_file(f"{base_dir}/lib/features/lawyer/screens/lawyer_profile_screen.dart", """import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import '../../../core/config/theme/app_theme.dart';

class LawyerProfileScreen extends StatelessWidget {
  final String lawyerId;
  const LawyerProfileScreen({super.key, required this.lawyerId});

  @override
  Widget build(BuildContext context) {
    return Scaffold(appBar: AppBar(title: const Text('Lawyer Profile')), body: SingleChildScrollView(child: Column(children: [
      const SizedBox(height: 24),
      const CircleAvatar(radius: 50, backgroundColor: AppTheme.yemeniGreen, child: Icon(Icons.person, size: 50, color: Colors.white)),
      const SizedBox(height: 16),
      const Text('Ahmed Ali', style: TextStyle(fontSize: 22, fontWeight: FontWeight.bold)),
      const Text('Lawyer', style: TextStyle(color: Colors.grey)),
      const SizedBox(height: 8),
      Row(mainAxisAlignment: MainAxisAlignment.center, children: [const Icon(Icons.star, color: Colors.amber, size: 20), const SizedBox(width: 4), const Text('4.8', style: TextStyle(fontWeight: FontWeight.bold)), const SizedBox(width: 16), const Icon(Icons.work_outline, size: 20), const SizedBox(width: 4), const Text('10 years')]),
      const SizedBox(height: 24),
      Padding(padding: const EdgeInsets.symmetric(horizontal: 24), child: Card(child: Padding(padding: const EdgeInsets.all(16), child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
        const Text('Specializations', style: TextStyle(fontWeight: FontWeight.bold, fontSize: 16)),
        const SizedBox(height: 8),
        Wrap(spacing: 8, runSpacing: 8, children: [_buildChip('Labor'), _buildChip('Personal'), _buildChip('Commercial')]),
        const SizedBox(height: 16),
        const Text('Bio', style: TextStyle(fontWeight: FontWeight.bold, fontSize: 16)),
        const SizedBox(height: 8),
        const Text('Licensed lawyer with 10+ years experience'),
      ])))),
      const SizedBox(height: 24),
      Padding(padding: const EdgeInsets.symmetric(horizontal: 24), child: SizedBox(width: double.infinity, child: ElevatedButton.icon(onPressed: () => context.push('/new-consultation'), icon: const Icon(Icons.chat), label: const Text('Request Consultation'), style: ElevatedButton.styleFrom(padding: const EdgeInsets.symmetric(vertical: 16))))),
      const SizedBox(height: 24),
    ])));
  }

  Widget _buildChip(String label) {
    return Chip(label: Text(label), backgroundColor: AppTheme.yemeniGreen.withOpacity(0.1), labelStyle: const TextStyle(color: AppTheme.yemeniGreen));
  }
}
""")

write_file(f"{base_dir}/lib/features/about/screens/about_screen.dart", """import 'package:flutter/material.dart';
import '../../../core/config/theme/app_theme.dart';

class AboutScreen extends StatelessWidget {
  const AboutScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(appBar: AppBar(title: const Text('About')), body: SingleChildScrollView(padding: const EdgeInsets.all(24), child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
      Center(child: Icon(Icons.balance, size: 80, color: AppTheme.yemeniGreen)),
      const SizedBox(height: 24),
      const Text('Hakki Yamani', style: TextStyle(fontSize: 28, fontWeight: FontWeight.bold, textAlign: TextAlign.center)),
      const SizedBox(height: 8),
      const Text('Your Legal Encyclopedia', style: TextStyle(fontSize: 16, color: Colors.grey), textAlign: TextAlign.center),
      const SizedBox(height: 32),
      _buildSection('Vision', 'To be the primary legal reference for every Yemeni citizen'),
      const SizedBox(height: 16),
      _buildSection('Mission', 'Provide reliable legal information and connect citizens with lawyers'),
      const SizedBox(height: 16),
      _buildSection('Goals', ['Spread legal culture', 'Comprehensive law database', 'Facilitate consultations', 'Support those in need']),
      const SizedBox(height: 32),
      const Center(child: Text('Version 1.0.0\\nAll rights reserved 2024', textAlign: TextAlign.center, style: TextStyle(color: Colors.grey))),
    ])));
  }

  Widget _buildSection(String title, dynamic content) {
    return Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
      Text(title, style: const TextStyle(fontSize: 20, fontWeight: FontWeight.bold, color: AppTheme.yemeniGreen)),
      const SizedBox(height: 8),
      if (content is String) Text(content, style: const TextStyle(fontSize: 16, height: 1.6))
      else if (content is List) ...content.map((item) => Padding(padding: const EdgeInsets.only(bottom: 4, right: 16), child: Row(children: [const Icon(Icons.check_circle, size: 16, color: AppTheme.yemeniGreen), const SizedBox(width: 8), Expanded(child: Text(item, style: const TextStyle(fontSize: 16)))]))),
    ]);
  }
}
""")

write_file(f"{base_dir}/lib/features/about/screens/privacy_screen.dart", """import 'package:flutter/material.dart';

class PrivacyScreen extends StatelessWidget {
  const PrivacyScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(appBar: AppBar(title: const Text('Privacy')), body: SingleChildScrollView(padding: const EdgeInsets.all(24), child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
      _buildHeading('Introduction'),
      _buildText('Welcome to Hakki Yamani. We protect your privacy.'),
      const SizedBox(height: 24),
      _buildHeading('Information We Collect'),
      _buildText('We collect name, email, phone during registration.'),
      const SizedBox(height: 24),
      _buildHeading('How We Use'),
      _buildList(['Provide consultations', 'Communicate with you', 'Improve app', 'Send notifications']),
      const SizedBox(height: 24),
      _buildHeading('Data Security'),
      _buildText('We use encryption to protect your data.'),
      const SizedBox(height: 24),
      _buildHeading('Contact'),
      _buildText('privacy@myyemeniright.com'),
    ])));
  }

  Widget _buildHeading(String title) => Text(title, style: const TextStyle(fontSize: 20, fontWeight: FontWeight.bold, color: Colors.green));
  Widget _buildText(String text) => Padding(padding: const EdgeInsets.only(top: 8), child: Text(text, style: const TextStyle(fontSize: 16, height: 1.6)));
  Widget _buildList(List<String> items) => Padding(padding: const EdgeInsets.only(top: 8), child: Column(children: items.map((item) => Padding(padding: const EdgeInsets.only(bottom: 4, right: 16), child: Row(children: [const Icon(Icons.arrow_left, size: 16, color: Colors.green), const SizedBox(width: 8), Expanded(child: Text(item, style: const TextStyle(fontSize: 16)))]))).toList()));
}
""")

write_file(f"{base_dir}/lib/features/about/screens/terms_screen.dart", """import 'package:flutter/material.dart';

class TermsScreen extends StatelessWidget {
  const TermsScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(appBar: AppBar(title: const Text('Terms')), body: SingleChildScrollView(padding: const EdgeInsets.all(24), child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
      const Text('Terms of Use', style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold)),
      const SizedBox(height: 24),
      _buildSection('1. Acceptance', 'By using Hakki Yamani, you agree to these terms.'),
      const SizedBox(height: 16),
      _buildSection('2. Service', 'The app provides legal information and consultations.'),
      const SizedBox(height: 16),
      _buildSection('3. Accounts', 'You are responsible for your account security.'),
      const SizedBox(height: 16),
      _buildSection('4. Intellectual Property', 'All content is protected by copyright.'),
      const SizedBox(height: 16),
      _buildSection('5. Disclaimer', 'The app does not replace professional legal advice.'),
    ])));
  }

  Widget _buildSection(String title, String content) => Column(crossAxisAlignment: CrossAxisAlignment.start, children: [Text(title, style: const TextStyle(fontSize: 18, fontWeight: FontWeight.bold)), const SizedBox(height: 8), Text(content, style: const TextStyle(fontSize: 16, height: 1.6))]);
}
""")

write_file(f"{base_dir}/lib/features/faq/screens/faq_screen.dart", """import 'package:flutter/material.dart';
import '../../../core/config/theme/app_theme.dart';

class FaqScreen extends StatelessWidget {
  const FaqScreen({super.key});
  final List<Map<String, String>> _faqs = const [
    {'q': 'How long is maternity leave?', 'a': '60 days according to Yemeni Labor Law'},
    {'q': 'What are women inheritance rights?', 'a': 'Guaranteed by law and Sharia'},
    {'q': 'Can employer fire without reason?', 'a': 'No, worker has right to compensation'},
    {'q': 'What is custody age?', 'a': '7 for boys, 9 for girls'},
    {'q': 'Disability rights in education?', 'a': 'Free and compulsory education with integration'},
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(appBar: AppBar(title: const Text('FAQ')), body: ListView.builder(padding: const EdgeInsets.all(16), itemCount: _faqs.length, itemBuilder: (context, index) {
      final faq = _faqs[index];
      return Card(margin: const EdgeInsets.only(bottom: 12), child: ExpansionTile(leading: CircleAvatar(backgroundColor: AppTheme.yemeniGreen.withOpacity(0.1), child: const Icon(Icons.help_outline, color: AppTheme.yemeniGreen)), title: Text(faq['q']!, style: const TextStyle(fontWeight: FontWeight.bold, fontSize: 16)), children: [Padding(padding: const EdgeInsets.fromLTRB(16, 0, 16, 16), child: Text(faq['a']!, style: const TextStyle(fontSize: 15, height: 1.6, color: Colors.black87)))]));
    }));
  }
}
""")

write_file(f"{base_dir}/android/build.gradle", """buildscript {
    ext.kotlin_version = '1.7.10'
    repositories {
        google()
        mavenCentral()
    }
    dependencies {
        classpath 'com.android.tools.build:gradle:7.3.0'
        classpath "org.jetbrains.kotlin:kotlin-gradle-plugin:\$kotlin_version"
        classpath 'com.google.gms:google-services:4.4.0'
    }
}

allprojects {
    repositories {
        google()
        mavenCentral()
    }
}

rootProject.buildDir = '../build'
subprojects {
    project.buildDir = "\${rootProject.buildDir}/\${project.name}"
}
subprojects {
    project.evaluationDependsOn(':app')
}

tasks.register("clean", Delete) {
    delete rootProject.buildDir
}
""")

write_file(f"{base_dir}/android/app/build.gradle", """plugins {
    id "com.android.application"
    id "kotlin-android"
    id "dev.flutter.flutter-gradle-plugin"
    id "com.google.gms.google-services"
}

def localProperties = new Properties()
def localPropertiesFile = rootProject.file('local.properties')
if (localPropertiesFile.exists()) {
    localPropertiesFile.withReader('UTF-8') { reader ->
        localProperties.load(reader)
    }
}

def flutterVersionCode = localProperties.getProperty('flutter.versionCode')
if (flutterVersionCode == null) {
    flutterVersionCode = '1'
}

def flutterVersionName = localProperties.getProperty('flutter.versionName')
if (flutterVersionName == null) {
    flutterVersionName = '1.0'
}

android {
    namespace "com.myemeniright.app"
    compileSdk 34
    ndkVersion flutter.ndkVersion

    compileOptions {
        sourceCompatibility JavaVersion.VERSION_1_8
        targetCompatibility JavaVersion.VERSION_1_8
    }

    kotlinOptions {
        jvmTarget = '1.8'
    }

    sourceSets {
        main.java.srcDirs += 'src/main/kotlin'
    }

    defaultConfig {
        applicationId "com.myemeniright.app"
        minSdk 21
        targetSdk 34
        versionCode flutterVersionCode.toInteger()
        versionName flutterVersionName
        multiDexEnabled true
    }

    buildTypes {
        release {
            signingConfig signingConfigs.debug
            minifyEnabled false
            shrinkResources false
        }
    }
}

flutter {
    source '../..'
}

dependencies {
    implementation platform('com.google.firebase:firebase-bom:32.7.0')
    implementation 'com.google.firebase:firebase-analytics'
}
""")

write_file(f"{base_dir}/android/app/src/main/AndroidManifest.xml", """<manifest xmlns:android="http://schemas.android.com/apk/res/android">
    <uses-permission android:name="android.permission.INTERNET"/>
    <uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE"/>
    <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE"/>
    <uses-permission android:name="android.permission.CAMERA"/>
    <uses-permission android:name="android.permission.RECEIVE_BOOT_COMPLETED"/>
    <uses-permission android:name="android.permission.VIBRATE"/>
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
              android:resource="@style/NormalTheme"
              />
            <intent-filter>
                <action android:name="android.intent.action.MAIN"/>
                <category android:name="android.intent.category.LAUNCHER"/>
            </intent-filter>
        </activity>
        <meta-data android:name="flutterEmbedding" android:value="2" />
    </application>
</manifest>
""")

write_file(f"{base_dir}/android/app/src/main/kotlin/com/myemeniright/app/MainActivity.kt", """package com.myemeniright.app

import io.flutter.embedding.android.FlutterActivity

class MainActivity: FlutterActivity() {
}
""")

write_file(f"{base_dir}/android/settings.gradle", """pluginManagement {
    def flutterSdkPath = {
        def properties = new Properties()
        file("local.properties").withInputStream { properties.load(it) }
        def flutterSdkPath = properties.getProperty("flutter.sdk")
        assert flutterSdkPath != null, "flutter.sdk not set in local.properties"
        return flutterSdkPath
    }
    settings.ext.flutterSdkPath = flutterSdkPath()

    includeBuild("\${settings.ext.flutterSdkPath}/packages/flutter_tools/gradle")

    repositories {
        google()
        mavenCentral()
        gradlePluginPortal()
    }

    plugins {
        id "dev.flutter.flutter-gradle-plugin" version "1.0.0" apply false
    }
}

plugins {
    id "dev.flutter.flutter-plugin-loader" version "1.0.0"
    id "com.android.application" version "7.3.0" apply false
    id "org.jetbrains.kotlin.android" version "1.7.10" apply false
    id "com.google.gms.google-services" version "4.4.0" apply false
}

include ":app"
""")

write_file(f"{base_dir}/lib/providers/auth_provider.dart", """import 'dart:async';
import 'package:flutter/material.dart';
import 'package:firebase_auth/firebase_auth.dart';
import 'package:cloud_firestore/cloud_firestore.dart';
import '../core/services/local_storage_service.dart';

class AuthProvider extends ChangeNotifier {
  final FirebaseAuth _auth = FirebaseAuth.instance;
  final FirebaseFirestore _firestore = FirebaseFirestore.instance;

  User? _currentUser;
  Map<String, dynamic>? _userData;
  bool _isLoading = false;
  String? _errorMessage;
  // FIX: Store subscription to cancel it on dispose
  StreamSubscription<User?>? _authSubscription;

  User? get currentUser => _currentUser;
  Map<String, dynamic>? get userData => _userData;
  bool get isLoading => _isLoading;
  String? get errorMessage => _errorMessage;
  bool get isAuthenticated => _currentUser != null;
  bool get isLawyer => _userData?['userType'] == 'lawyer';

  AuthProvider() {
    // FIX: Store the subscription so we can cancel it later
    _authSubscription = _auth.authStateChanges().listen(_onAuthStateChanged);
  }

  // FIX: Override dispose to cancel the listener and prevent memory leaks
  @override
  void dispose() {
    _authSubscription?.cancel();
    super.dispose();
  }

  void _onAuthStateChanged(User? user) {
    _currentUser = user;
    if (user != null) {
      _loadUserData();
    } else {
      _userData = null;
      notifyListeners();
    }
  }

  Future<void> _loadUserData() async {
    if (_currentUser == null) return;
    try {
      // FIX: Use safe null access instead of ! operator
      final uid = _currentUser?.uid;
      if (uid == null) return;
      final doc = await _firestore.collection('users').doc(uid).get();
      if (doc.exists) {
        _userData = doc.data();
        final userType = _userData?['userType'];
        if (userType != null) {
          await LocalStorageService.saveUserData('userType', userType);
        }
      }
    } catch (e) {
      _errorMessage = e.toString();
    }
    notifyListeners();
  }

  Future<bool> signInWithPhone(String phoneNumber) async {
    _isLoading = true;
    _errorMessage = null;
    notifyListeners();
    try {
      await _auth.verifyPhoneNumber(
        phoneNumber: phoneNumber,
        verificationCompleted: (PhoneAuthCredential credential) async {
          await _auth.signInWithCredential(credential);
        },
        verificationFailed: (FirebaseAuthException e) {
          _errorMessage = e.message ?? 'Verification failed';
          _isLoading = false;
          notifyListeners();
        },
        codeSent: (String verificationId, int? resendToken) async {
          // FIX: Await the async operation
          await LocalStorageService.saveUserData('verificationId', verificationId);
          _isLoading = false;
          notifyListeners();
        },
        codeAutoRetrievalTimeout: (String verificationId) async {
          // FIX: Await the async operation
          await LocalStorageService.saveUserData('verificationId', verificationId);
        },
      );
      return true;
    } catch (e) {
      _errorMessage = e.toString();
      _isLoading = false;
      notifyListeners();
      return false;
    }
  }

  Future<bool> verifyOtp(String otpCode) async {
    _isLoading = true;
    _errorMessage = null;
    notifyListeners();
    try {
      // FIX: Check for null before using verificationId
      final verificationId = LocalStorageService.getUserData('verificationId') as String?;
      if (verificationId == null || verificationId.isEmpty) {
        _errorMessage = 'Verification ID not found. Please request a new code.';
        _isLoading = false;
        notifyListeners();
        return false;
      }
      final credential = PhoneAuthProvider.credential(
        verificationId: verificationId,
        smsCode: otpCode,
      );
      await _auth.signInWithCredential(credential);
      _isLoading = false;
      notifyListeners();
      return true;
    } catch (e) {
      _errorMessage = 'Invalid OTP or verification expired';
      _isLoading = false;
      notifyListeners();
      return false;
    }
  }

  Future<bool> signInWithEmail(String email, String password) async {
    _isLoading = true;
    _errorMessage = null;
    notifyListeners();
    try {
      await _auth.signInWithEmailAndPassword(email: email, password: password);
      _isLoading = false;
      notifyListeners();
      return true;
    } catch (e) {
      _errorMessage = 'Invalid email or password';
      _isLoading = false;
      notifyListeners();
      return false;
    }
  }

  Future<bool> registerWithEmail(String email, String password, String fullName, String phoneNumber, {String? userType = 'citizen'}) async {
    _isLoading = true;
    _errorMessage = null;
    notifyListeners();
    try {
      final credential = await _auth.createUserWithEmailAndPassword(email: email, password: password);
      final uid = credential.user?.uid;
      if (uid == null) throw Exception('User creation failed');
      await _firestore.collection('users').doc(uid).set({
        'uid': uid,
        'userType': userType,
        'phoneNumber': phoneNumber,
        'email': email,
        'fullName': fullName,
        'createdAt': FieldValue.serverTimestamp(),
        'lastLogin': FieldValue.serverTimestamp(),
        'isVerified': false,
        'savedLaws': [],
        'bookmarks': [],
      });
      _isLoading = false;
      notifyListeners();
      return true;
    } catch (e) {
      _errorMessage = 'Registration failed: ${e.toString()}';
      _isLoading = false;
      notifyListeners();
      return false;
    }
  }

  Future<void> signOut() async {
    try {
      await _auth.signOut();
      await LocalStorageService.clearAll();
    } catch (e) {
      _errorMessage = e.toString();
      notifyListeners();
    }
  }

  Future<void> updateProfile(Map<String, dynamic> data) async {
    try {
      final uid = _currentUser?.uid;
      if (uid == null) return;
      await _firestore.collection('users').doc(uid).update(data);
      await _loadUserData();
    } catch (e) {
      _errorMessage = e.toString();
      notifyListeners();
    }
  }
}
""")

write_file(f"{base_dir}/lib/features/laws/screens/law_detail_screen.dart", """import 'package:flutter/material.dart';
import '../../../core/config/theme/app_theme.dart';

class LawDetailScreen extends StatefulWidget {
  final String lawId;
  const LawDetailScreen({super.key, required this.lawId});
  @override
  State<LawDetailScreen> createState() => _LawDetailScreenState();
}

class _LawDetailScreenState extends State<LawDetailScreen> {
  bool _isFavorite = false;
  final List<Map<String, dynamic>> _articles = [
    {'number': 1, 'title': 'Article 1', 'content': 'Yemen is an independent Arab Islamic state with full sovereignty...'},
    {'number': 2, 'title': 'Article 2', 'content': 'Islam is the state religion, and Islamic Sharia is the source of all legislation...'},
    {'number': 3, 'title': 'Article 3', 'content': 'Arabic is the official language of the state...'},
  ];

  @override
  Widget build(BuildContext context) {
    // FIX: Removed Expanded - ListView.builder can be direct child of Scaffold body
    return Scaffold(
      appBar: AppBar(
        title: const Text('Yemen Constitution'),
        actions: [
          IconButton(
            icon: Icon(_isFavorite ? Icons.favorite : Icons.favorite_border),
            onPressed: () => setState(() => _isFavorite = !_isFavorite),
          ),
          IconButton(
            icon: const Icon(Icons.share),
            onPressed: () {},
          ),
        ],
      ),
      body: ListView.builder(
        padding: const EdgeInsets.all(16),
        itemCount: _articles.length,
        itemBuilder: (context, index) {
          final article = _articles[index];
          return Card(
            margin: const EdgeInsets.only(bottom: 12),
            child: ExpansionTile(
              leading: CircleAvatar(
                backgroundColor: AppTheme.yemeniGreen,
                child: Text(
                  '${article['number']}',
                  style: const TextStyle(color: Colors.white, fontWeight: FontWeight.bold),
                ),
              ),
              title: Text(
                article['title'],
                style: const TextStyle(fontFamily: 'Cairo', fontWeight: FontWeight.bold),
              ),
              subtitle: Text(
                article['content'].substring(0, 50) + '...',
                maxLines: 1,
                overflow: TextOverflow.ellipsis,
              ),
              children: [
                Padding(
                  padding: const EdgeInsets.all(16),
                  child: Text(
                    article['content'],
                    style: const TextStyle(fontFamily: 'Cairo', fontSize: 16, height: 1.8),
                  ),
                ),
              ],
            ),
          );
        },
      ),
    );
  }
}
""")

write_file(f"{base_dir}/lib/features/consultations/screens/consultation_detail_screen.dart", """import 'package:flutter/material.dart';
import '../../../core/config/theme/app_theme.dart';

class ConsultationDetailScreen extends StatefulWidget {
  final String consultationId;
  const ConsultationDetailScreen({super.key, required this.consultationId});
  @override
  State<ConsultationDetailScreen> createState() => _ConsultationDetailScreenState();
}

class _ConsultationDetailScreenState extends State<ConsultationDetailScreen> {
  final _messageController = TextEditingController();
  final ScrollController _scrollController = ScrollController();
  final List<Map<String, dynamic>> _messages = [
    {'id': '1', 'senderId': 'client', 'content': 'Hello, I have a question', 'time': '10:30'},
    {'id': '2', 'senderId': 'lawyer', 'content': 'Welcome, ask your question', 'time': '10:35'},
  ];

  @override
  void dispose() {
    _messageController.dispose();
    _scrollController.dispose();
    super.dispose();
  }

  void _sendMessage() {
    if (_messageController.text.isEmpty) return;
    setState(() {
      _messages.add({
        'id': DateTime.now().millisecondsSinceEpoch.toString(),
        'senderId': 'client',
        'content': _messageController.text,
        'time': '${DateTime.now().hour}:${DateTime.now().minute}',
      });
    });
    _messageController.clear();
    Future.delayed(const Duration(milliseconds: 100), () {
      // FIX: Check if controller is attached before scrolling
      if (_scrollController.hasClients) {
        _scrollController.animateTo(
          _scrollController.position.maxScrollExtent,
          duration: const Duration(milliseconds: 300),
          curve: Curves.easeOut,
        );
      }
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text('Consultation'),
            Text('Ahmed Ali', style: TextStyle(fontSize: 12, fontWeight: FontWeight.normal)),
          ],
        ),
        actions: [
          IconButton(icon: const Icon(Icons.attach_file), onPressed: () {}),
          IconButton(icon: const Icon(Icons.more_vert), onPressed: () {}),
        ],
      ),
      body: Column(
        children: [
          Expanded(
            child: ListView.builder(
              controller: _scrollController,
              padding: const EdgeInsets.all(16),
              itemCount: _messages.length,
              itemBuilder: (context, index) {
                final message = _messages[index];
                final isMe = message['senderId'] == 'client';
                return Align(
                  alignment: isMe ? Alignment.centerLeft : Alignment.centerRight,
                  child: Container(
                    margin: const EdgeInsets.only(bottom: 12),
                    padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 10),
                    decoration: BoxDecoration(
                      color: isMe ? AppTheme.yemeniGreen : Colors.grey.shade200,
                      borderRadius: BorderRadius.only(
                        topLeft: const Radius.circular(12),
                        topRight: const Radius.circular(12),
                        bottomLeft: Radius.circular(isMe ? 12 : 0),
                        bottomRight: Radius.circular(isMe ? 0 : 12),
                      ),
                    ),
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Text(message['content'], style: TextStyle(color: isMe ? Colors.white : Colors.black)),
                        const SizedBox(height: 4),
                        Text(message['time'], style: TextStyle(fontSize: 10, color: isMe ? Colors.white70 : Colors.black54)),
                      ],
                    ),
                  ),
                );
              },
            ),
          ),
          Container(
            padding: const EdgeInsets.all(16),
            decoration: BoxDecoration(
              color: Colors.white,
              boxShadow: [BoxShadow(color: Colors.black.withOpacity(0.1), blurRadius: 4, offset: const Offset(0, -2))],
            ),
            child: Row(
              children: [
                Expanded(
                  child: TextField(
                    controller: _messageController,
                    decoration: InputDecoration(
                      hintText: 'Type message...',
                      border: OutlineInputBorder(borderRadius: BorderRadius.circular(24)),
                      contentPadding: const EdgeInsets.symmetric(horizontal: 20, vertical: 12),
                    ),
                    maxLines: null,
                    textInputAction: TextInputAction.send,
                    onSubmitted: (_) => _sendMessage(),
                  ),
                ),
                const SizedBox(width: 8),
                CircleAvatar(
                  backgroundColor: AppTheme.yemeniGreen,
                  child: IconButton(
                    icon: const Icon(Icons.send, color: Colors.white),
                    onPressed: _sendMessage,
                  ),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
""")

write_file(f"{base_dir}/README.md", """# Hakki Yamani - My Yemeni Right

## Requirements
- Flutter 3.10+
- Dart 3.0+
- Android Studio or VS Code

## Fixes Applied (2026-07-01)
1. **Memory Leak Fix**: AuthProvider now properly cancels authStateChanges listener
2. **Null Safety**: Added null checks in verifyOtp() and _loadUserData()
3. **Provider Setup**: Added MultiProvider in main.dart
4. **LocalStorage Init**: Added LocalStorageService.init() in main()
5. **Widget Tree Fix**: Removed incorrect Expanded in law_detail_screen
6. **Scroll Safety**: Added hasClients check in consultation_detail_screen

## Build
1. Install dependencies
```bash
flutter pub get
```

2. Run the app
```bash
flutter run
```

## Firebase Setup
1. Add your `google-services.json` to `android/app/`
2. Add your `GoogleService-Info.plist` to `ios/Runner/`

## Features
- Legal encyclopedia with Yemen laws
- Lawyer consultations
- Phone & Email authentication
- RTL Arabic interface
- Dark/Light theme support
""")
