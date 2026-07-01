import os
import urllib.request

print("جاري إنشاء مشروع 'حقي كيمني' - النسخة الكاملة...")
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
    print(f"OK: {dir_path.replace(base_dir + '/', '')}")

def write_file(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"OK: {path.replace(base_dir + '/', '')}")

print("\nجاري توليد صورة الشعار...")
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
        (size//2, 80),
        (size - 120, 150),
        (size - 120, size//2 + 100),
        (size//2, size - 80),
        (120, size//2 + 100),
        (120, 150),
    ]
    draw.polygon(shield_points, fill=yemeni_green, outline=gold, width=15)

    stripe_height = (size - 260) // 3
    draw.rectangle([140, 170, size-140, 170+stripe_height], fill=yemeni_red)
    draw.rectangle([140, 170+stripe_height, size-140, 170+stripe_height*2], fill=yemeni_white)
    draw.rectangle([140, 170+stripe_height*2, size-140, 170+stripe_height*3], fill=yemeni_black)

    center_x = size // 2
    draw.rectangle([center_x-15, 280, center_x+15, 700], fill=gold, outline=yemeni_black, width=3)
    draw.rectangle([center_x-120, 700, center_x+120, 730], fill=gold, outline=yemeni_black, width=3)
    draw.rectangle([center_x-150, 730, center_x+150, 760], fill=gold, outline=yemeni_black, width=3)
    draw.rectangle([180, 280, size-180, 310], fill=gold, outline=yemeni_black, width=3)
    draw.ellipse([center_x-25, 240, center_x+25, 290], fill=gold, outline=yemeni_black, width=3)

    draw.line([220, 310, 220, 500], fill=gold, width=8)
    draw.line([180, 500, 260, 500], fill=gold, width=8)
    draw.polygon([(180, 500), (260, 500), (240, 620), (200, 620)], fill=gold, outline=yemeni_black, width=3)

    draw.line([size-220, 310, size-220, 500], fill=gold, width=8)
    draw.line([size-260, 500, size-180, 500], fill=gold, width=8)
    draw.polygon([(size-260, 500), (size-180, 500), (size-200, 620), (size-240, 620)], fill=gold, outline=yemeni_black, width=3)

    draw.ellipse([170, 270, 230, 330], fill=gold, outline=yemeni_black, width=3)
    draw.ellipse([size-230, 270, size-170, 330], fill=gold, outline=yemeni_black, width=3)

    icons_dir = f"{base_dir}/assets/icons"
    images_dir = f"{base_dir}/assets/images"

    img.save(f"{icons_dir}/app_icon.png", "PNG")
    img.save(f"{images_dir}/logo.png", "PNG")

    bg_img = Image.new('RGBA', (size, size), yemeni_green)
    bg_img.paste(img, (0, 0), img)
    bg_img.save(f"{icons_dir}/app_icon_bg.png", "PNG")

    print("تم توليد الشعار بنجاح!")
except ImportError:
    print("مكتبة Pillow غير مثبتة. جاري تثبيتها...")
    os.system("pip install Pillow")
    print("تم تثبيت Pillow. يرجى إعادة تشغيل السكريبت.")
    exit()

print("\nجاري تحميل الخطوط العربية...")
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
        print(f"تحميل {font_name}...")
        urllib.request.urlretrieve(font_url, font_path)
        print(f"تم تحميل {font_name}")
    except Exception as e:
        print(f"فشل تحميل {font_name}: {e}")
print("\nتم تحميل الخطوط!")

write_file(f"{base_dir}/pubspec.yaml", """name: my_yemeni_right
description: حقي كيمني - التطبيق القانوني الشامل للمواطن اليمني
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
  firebase_storage: ^11.5.0
  firebase_messaging: ^14.7.0
  hive: ^2.2.3
  hive_flutter: ^1.1.0
  path_provider: ^2.1.1
  cupertino_icons: ^1.0.6
  flutter_svg: ^2.0.9
  cached_network_image: ^3.3.0
  shimmer: ^3.0.0
  flutter_form_builder: ^9.1.1
  form_builder_validators: ^9.1.0
  url_launcher: ^6.2.1
  share_plus: ^7.2.1
  image_picker: ^1.0.5
  file_picker: ^6.1.1
  permission_handler: ^11.0.1
  dio: ^5.4.0
  connectivity_plus: ^5.0.2
  pin_code_fields: ^8.0.1
  font_awesome_flutter: ^10.6.0
  lottie: ^2.7.0
  animate_do: ^3.1.2

dev_dependencies:
  flutter_test:
    sdk: flutter
  flutter_lints: ^3.0.1
  hive_generator: ^2.0.1
  build_runner: ^2.4.7
  flutter_launcher_icons: ^0.13.1

flutter:
  uses-material-design: true
  assets:
    - assets/images/
    - assets/icons/
    - assets/laws/
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

flutter_icons:
  android: true
  ios: true
  image_path: "assets/icons/app_icon.png"
  adaptive_icon_background: "#1B5E20"
""")

write_file(f"{base_dir}/lib/main.dart", """import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_localizations/flutter_localizations.dart';
import 'package:firebase_core/firebase_core.dart';
import 'package:hive_flutter/hive_flutter.dart';
import 'package:provider/provider.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'core/config/routes.dart';
import 'core/config/theme/app_theme.dart';
import 'core/services/local_storage_service.dart';
import 'providers/auth_provider.dart';
import 'providers/law_provider.dart';
import 'providers/consultation_provider.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp();
  await Hive.initFlutter();
  await LocalStorageService.init();
  await SystemChrome.setPreferredOrientations([
    DeviceOrientation.portraitUp,
    DeviceOrientation.portraitDown,
  ]);
  runApp(const ProviderScope(child: MyApp()));
}

class MyApp extends ConsumerWidget {
  const MyApp({super.key});
  @override
  Widget build(BuildContext context, WidgetRef ref) {
    return MultiProvider(
      providers: [
        ChangeNotifierProvider(create: (_) => AuthProvider()),
        ChangeNotifierProvider(create: (_) => LawProvider()),
        ChangeNotifierProvider(create: (_) => ConsultationProvider()),
      ],
      child: MaterialApp.router(
        title: 'حقي كيمني',
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
      appBar: AppBar(title: const Text('خطأ')),
      body: const Center(child: Text('الصفحة غير موجودة')),
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

write_file(f"{base_dir}/lib/providers/auth_provider.dart", """import 'package:flutter/material.dart';
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

  User? get currentUser => _currentUser;
  Map<String, dynamic>? get userData => _userData;
  bool get isLoading => _isLoading;
  String? get errorMessage => _errorMessage;
  bool get isAuthenticated => _currentUser != null;
  bool get isLawyer => _userData?['userType'] == 'lawyer';

  AuthProvider() {
    _auth.authStateChanges().listen(_onAuthStateChanged);
  }

  void _onAuthStateChanged(User? user) {
    _currentUser = user;
    if (user != null) {
      _loadUserData();
    } else {
      _userData = null;
    }
    notifyListeners();
  }

  Future<void> _loadUserData() async {
    if (_currentUser == null) return;
    try {
      final doc = await _firestore.collection('users').doc(_currentUser!.uid).get();
      if (doc.exists) {
        _userData = doc.data();
        await LocalStorageService.saveUserData('userType', _userData!['userType']);
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
          _errorMessage = e.message;
          _isLoading = false;
          notifyListeners();
        },
        codeSent: (String verificationId, int? resendToken) {
          LocalStorageService.saveUserData('verificationId', verificationId);
          _isLoading = false;
          notifyListeners();
        },
        codeAutoRetrievalTimeout: (String verificationId) {
          LocalStorageService.saveUserData('verificationId', verificationId);
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
      final verificationId = LocalStorageService.getUserData('verificationId');
      final credential = PhoneAuthProvider.credential(
        verificationId: verificationId,
        smsCode: otpCode,
      );
      await _auth.signInWithCredential(credential);
      _isLoading = false;
      notifyListeners();
      return true;
    } catch (e) {
      _errorMessage = 'رمز التحقق غير صحيح';
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
      _errorMessage = 'البريد الإلكتروني أو كلمة المرور غير صحيحة';
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
      await _firestore.collection('users').doc(credential.user!.uid).set({
        'uid': credential.user!.uid,
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
      _errorMessage = 'حدث خطأ أثناء التسجيل';
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
      await _firestore.collection('users').doc(_currentUser!.uid).update(data);
      await _loadUserData();
    } catch (e) {
      _errorMessage = e.toString();
      notifyListeners();
    }
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
      throw Exception('فشل في إنشاء الاستشارة');
    }
  }
}
""")

write_file(f"{base_dir}/lib/features/auth/screens/login_screen.dart", """import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:go_router/go_router.dart';
import '../../../providers/auth_provider.dart';
import '../../../core/config/theme/app_theme.dart';

class LoginScreen extends ConsumerStatefulWidget {
  const LoginScreen({super.key});
  @override
  ConsumerState<LoginScreen> createState() => _LoginScreenState();
}

class _LoginScreenState extends ConsumerState<LoginScreen> {
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
    final success = await ref.read(authProvider).signInWithEmail(
      _emailController.text.trim(),
      _passwordController.text,
    );
    if (success && mounted) {
      context.go('/');
    } else if (mounted) {
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(content: Text(ref.read(authProvider).errorMessage ?? 'حدث خطأ'), backgroundColor: AppTheme.yemeniRed),
      );
    }
  }

  @override
  Widget build(BuildContext context) {
    final authState = ref.watch(authProvider);
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
              const Text('حقي كيمني', textAlign: TextAlign.center, style: TextStyle(fontFamily: 'Cairo', fontSize: 32, fontWeight: FontWeight.bold, color: AppTheme.yemeniGreen)),
              const SizedBox(height: 8),
              const Text('تسجيل الدخول', textAlign: TextAlign.center, style: TextStyle(fontFamily: 'Cairo', fontSize: 18, color: AppTheme.textSecondaryLight)),
              const SizedBox(height: 48),
              Form(
                key: _formKey,
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.stretch,
                  children: [
                    TextFormField(controller: _emailController, keyboardType: TextInputType.emailAddress, decoration: const InputDecoration(labelText: 'البريد الإلكتروني', prefixIcon: Icon(Icons.email_outlined)), validator: (value) {
                      if (value == null || value.isEmpty) return 'الرجاء إدخال البريد الإلكتروني';
                      if (!value.contains('@')) return 'البريد الإلكتروني غير صحيح';
                      return null;
                    }),
                    const SizedBox(height: 16),
                    TextFormField(controller: _passwordController, obscureText: _obscurePassword, decoration: InputDecoration(labelText: 'كلمة المرور', prefixIcon: const Icon(Icons.lock_outlined), suffixIcon: IconButton(icon: Icon(_obscurePassword ? Icons.visibility_outlined : Icons.visibility_off_outlined), onPressed: () => setState(() => _obscurePassword = !_obscurePassword))), validator: (value) {
                      if (value == null || value.isEmpty) return 'الرجاء إدخال كلمة المرور';
                      return null;
                    }),
                    const SizedBox(height: 24),
                    ElevatedButton(onPressed: authState.isLoading ? null : _handleLogin, child: authState.isLoading ? const SizedBox(height: 20, width: 20, child: CircularProgressIndicator(strokeWidth: 2, color: Colors.white)) : const Text('تسجيل الدخول')),
                    const SizedBox(height: 24),
                    const Row(children: [Expanded(child: Divider()), Padding(padding: EdgeInsets.symmetric(horizontal: 16), child: Text('أو')), Expanded(child: Divider())]),
                    const SizedBox(height: 24),
                    OutlinedButton.icon(onPressed: () => context.push('/otp'), icon: const Icon(Icons.phone_android), label: const Text('الدخول برقم الهاتف'), style: OutlinedButton.styleFrom(padding: const EdgeInsets.symmetric(vertical: 16))),
                    const SizedBox(height: 24),
                    Row(mainAxisAlignment: MainAxisAlignment.center, children: [const Text('ليس لديك حساب؟'), TextButton(onPressed: () => context.push('/register'), child: const Text('إنشاء حساب جديد', style: TextStyle(fontWeight: FontWeight.bold)))]),
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
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:go_router/go_router.dart';
import '../../../providers/auth_provider.dart';
import '../../../core/config/theme/app_theme.dart';

class RegisterScreen extends ConsumerStatefulWidget {
  const RegisterScreen({super.key});
  @override
  ConsumerState<RegisterScreen> createState() => _RegisterScreenState();
}

class _RegisterScreenState extends ConsumerState<RegisterScreen> {
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
      ScaffoldMessenger.of(context).showSnackBar(const SnackBar(content: Text('كلمات المرور غير متطابقة'), backgroundColor: AppTheme.yemeniRed));
      return;
    }
    final success = await ref.read(authProvider).registerWithEmail(
      _emailController.text.trim(),
      _passwordController.text,
      _fullNameController.text.trim(),
      _phoneController.text.trim(),
      userType: _userType,
    );
    if (success && mounted) {
      ScaffoldMessenger.of(context).showSnackBar(const SnackBar(content: Text('تم إنشاء الحساب بنجاح'), backgroundColor: AppTheme.yemeniGreen));
      context.go('/');
    } else if (mounted) {
      ScaffoldMessenger.of(context).showSnackBar(SnackBar(content: Text(ref.read(authProvider).errorMessage ?? 'حدث خطأ'), backgroundColor: AppTheme.yemeniRed));
    }
  }

  @override
  Widget build(BuildContext context) {
    final authState = ref.watch(authProvider);
    return Scaffold(
      appBar: AppBar(title: const Text('إنشاء حساب جديد'), leading: IconButton(icon: const Icon(Icons.arrow_back), onPressed: () => context.pop())),
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
                const Text('انضم إلينا الآن', textAlign: TextAlign.center, style: TextStyle(fontFamily: 'Cairo', fontSize: 24, fontWeight: FontWeight.bold)),
                const SizedBox(height: 32),
                TextFormField(controller: _fullNameController, decoration: const InputDecoration(labelText: 'الاسم الكامل', prefixIcon: Icon(Icons.person_outline)), validator: (value) => value == null || value.isEmpty ? 'الرجاء إدخال الاسم الكامل' : null),
                const SizedBox(height: 16),
                TextFormField(controller: _emailController, keyboardType: TextInputType.emailAddress, decoration: const InputDecoration(labelText: 'البريد الإلكتروني', prefixIcon: Icon(Icons.email_outlined)), validator: (value) {
                  if (value == null || value.isEmpty) return 'الرجاء إدخال البريد الإلكتروني';
                  if (!value.contains('@')) return 'البريد الإلكتروني غير صحيح';
                  return null;
                }),
                const SizedBox(height: 16),
                TextFormField(controller: _phoneController, keyboardType: TextInputType.phone, decoration: const InputDecoration(labelText: 'رقم الهاتف', prefixIcon: Icon(Icons.phone_outlined), hintText: '+967xxxxxxxxx'), validator: (value) => value == null || value.isEmpty ? 'الرجاء إدخال رقم الهاتف' : null),
                const SizedBox(height: 16),
                TextFormField(controller: _passwordController, obscureText: _obscurePassword, decoration: InputDecoration(labelText: 'كلمة المرور', prefixIcon: const Icon(Icons.lock_outlined), suffixIcon: IconButton(icon: Icon(_obscurePassword ? Icons.visibility_outlined : Icons.visibility_off_outlined), onPressed: () => setState(() => _obscurePassword = !_obscurePassword))), validator: (value) {
                  if (value == null || value.isEmpty) return 'الرجاء إدخال كلمة المرور';
                  if (value.length < 6) return 'كلمة المرور يجب أن تكون 6 أحرف على الأقل';
                  return null;
                }),
                const SizedBox(height: 16),
                TextFormField(controller: _confirmPasswordController, obscureText: _obscureConfirmPassword, decoration: InputDecoration(labelText: 'تأكيد كلمة المرور', prefixIcon: const Icon(Icons.lock_outlined), suffixIcon: IconButton(icon: Icon(_obscureConfirmPassword ? Icons.visibility_outlined : Icons.visibility_off_outlined), onPressed: () => setState(() => _obscureConfirmPassword = !_obscureConfirmPassword))), validator: (value) => value == null || value.isEmpty ? 'الرجاء تأكيد كلمة المرور' : null),
                const SizedBox(height: 24),
                const Text('نوع الحساب', style: TextStyle(fontFamily: 'Cairo', fontSize: 16, fontWeight: FontWeight.bold)),
                const SizedBox(height: 12),
                Row(children: [
                  Expanded(child: RadioListTile<String>(title: const Text('مواطن'), value: 'citizen', groupValue: _userType, onChanged: (value) => setState(() => _userType = value!))),
                  Expanded(child: RadioListTile<String>(title: const Text('محامٍ'), value: 'lawyer', groupValue: _userType, onChanged: (value) => setState(() => _userType = value!))),
                ]),
                const SizedBox(height: 24),
                ElevatedButton(onPressed: authState.isLoading ? null : _handleRegister, child: authState.isLoading ? const SizedBox(height: 20, width: 20, child: CircularProgressIndicator(strokeWidth: 2, color: Colors.white)) : const Text('إنشاء الحساب')),
                const SizedBox(height: 16),
                Row(mainAxisAlignment: MainAxisAlignment.center, children: [const Text('لديك حساب بالفعل؟'), TextButton(onPressed: () => context.pop(), child: const Text('تسجيل الدخول', style: TextStyle(fontWeight: FontWeight.bold)))]),
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
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:go_router/go_router.dart';
import 'package:pin_code_fields/pin_code_fields.dart';
import '../../../providers/auth_provider.dart';
import '../../../core/config/theme/app_theme.dart';

class OtpScreen extends ConsumerStatefulWidget {
  const OtpScreen({super.key});
  @override
  ConsumerState<OtpScreen> createState() => _OtpScreenState();
}

class _OtpScreenState extends ConsumerState<OtpScreen> {
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
      ScaffoldMessenger.of(context).showSnackBar(const SnackBar(content: Text('الرجاء إدخال رقم الهاتف'), backgroundColor: AppTheme.yemeniRed));
      return;
    }
    final success = await ref.read(authProvider).signInWithPhone('+967${_phoneController.text}');
    if (success && mounted) setState(() => _isCodeSent = true);
  }

  Future<void> _verifyOtp() async {
    final success = await ref.read(authProvider).verifyOtp(_currentCode);
    if (success && mounted) {
      context.go('/');
    } else if (mounted) {
      ScaffoldMessenger.of(context).showSnackBar(SnackBar(content: Text(ref.read(authProvider).errorMessage ?? 'رمز غير صحيح'), backgroundColor: AppTheme.yemeniRed));
    }
  }

  @override
  Widget build(BuildContext context) {
    final authState = ref.watch(authProvider);
    return Scaffold(
      appBar: AppBar(title: const Text('التحقق من رقم الهاتف'), leading: IconButton(icon: const Icon(Icons.arrow_back), onPressed: () => context.pop())),
      body: SafeArea(
        child: Padding(
          padding: const EdgeInsets.all(24),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: [
              const SizedBox(height: 40),
              Icon(Icons.phone_android, size: 80, color: AppTheme.yemeniGreen),
              const SizedBox(height: 24),
              const Text('التحقق من رقم الهاتف', textAlign: TextAlign.center, style: TextStyle(fontFamily: 'Cairo', fontSize: 24, fontWeight: FontWeight.bold)),
              const SizedBox(height: 16),
              Text(_isCodeSent ? 'أدخل رمز التحقق المرسل إلى ${_phoneController.text}' : 'أدخل رقم هاتفك للتحقق', textAlign: TextAlign.center, style: const TextStyle(fontFamily: 'Cairo', fontSize: 16, color: AppTheme.textSecondaryLight)),
              const SizedBox(height: 40),
              if (!_isCodeSent) ...[
                TextField(controller: _phoneController, keyboardType: TextInputType.phone, textAlign: TextAlign.center, decoration: const InputDecoration(labelText: 'رقم الهاتف', hintText: 'xxxxxxxxx', prefixText: '+967 ')),
                const SizedBox(height: 24),
                ElevatedButton(onPressed: authState.isLoading ? null : _sendOtp, child: authState.isLoading ? const CircularProgressIndicator(color: Colors.white) : const Text('إرسال رمز التحقق')),
              ] else ...[
                PinCodeTextField(appContext: context, length: 6, obscureText: false, animationType: AnimationType.fade, keyboardType: TextInputType.number, pinTheme: PinTheme(shape: PinCodeFieldShape.box, borderRadius: BorderRadius.circular(12), fieldHeight: 60, fieldWidth: 50, activeFillColor: Colors.white, inactiveFillColor: Colors.grey.shade100, selectedFillColor: Colors.white, activeColor: AppTheme.yemeniGreen, inactiveColor: Colors.grey, selectedColor: AppTheme.yemeniGreen), animationDuration: const Duration(milliseconds: 300), backgroundColor: Colors.transparent, enableActiveFill: true, onChanged: (value) => setState(() => _currentCode = value)),
                const SizedBox(height: 32),
                ElevatedButton(onPressed: authState.isLoading ? null : _verifyOtp, child: authState.isLoading ? const CircularProgressIndicator(color: Colors.white) : const Text('تحقق')),
                const SizedBox(height: 16),
                TextButton(onPressed: () => setState(() => _isCodeSent = false), child: const Text('تغيير رقم الهاتف')),
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
        NavigationDestination(icon: Icon(Icons.home_outlined), selectedIcon: Icon(Icons.home), label: 'الرئيسية'),
        NavigationDestination(icon: Icon(Icons.library_books_outlined), selectedIcon: Icon(Icons.library_books), label: 'القوانين'),
        NavigationDestination(icon: Icon(Icons.chat_outlined), selectedIcon: Icon(Icons.chat), label: 'الاستشارات'),
        NavigationDestination(icon: Icon(Icons.person_outline), selectedIcon: Icon(Icons.person), label: 'حسابي'),
      ],
    ));
  }
}

class HomeTab extends StatelessWidget {
  const HomeTab({super.key});
  @override
  Widget build(BuildContext context) {
    return CustomScrollView(slivers: [
      SliverAppBar(floating: true, title: const Text('حقي كيمني'), actions: [IconButton(icon: const Icon(Icons.search), onPressed: () => context.push('/search')), IconButton(icon: const Icon(Icons.notifications_outlined), onPressed: () {})]),
      SliverToBoxAdapter(child: Container(decoration: const BoxDecoration(gradient: LinearGradient(colors: [AppTheme.yemeniGreen, AppTheme.lightGreen], begin: Alignment.topRight, end: Alignment.bottomLeft)), padding: const EdgeInsets.all(24), child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
        const Text('مرحباً بك', style: TextStyle(color: Colors.white, fontSize: 24, fontWeight: FontWeight.bold)),
        const SizedBox(height: 8),
        const Text('موسوعتك القانونية الشاملة', style: TextStyle(color: Colors.white70, fontSize: 16)),
        const SizedBox(height: 16),
        Row(children: [
          Expanded(child: ElevatedButton.icon(onPressed: () => context.push('/laws'), icon: const Icon(Icons.search), label: const Text('ابحث في القوانين'), style: ElevatedButton.styleFrom(backgroundColor: Colors.white, foregroundColor: AppTheme.yemeniGreen))),
          const SizedBox(width: 12),
          ElevatedButton.icon(onPressed: () => context.push('/new-consultation'), icon: const Icon(Icons.add), label: const Text('استشارة')),
        ]),
      ]))),
      SliverPadding(padding: const EdgeInsets.all(16), sliver: SliverGrid(gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(crossAxisCount: 2, childAspectRatio: 1.2, crossAxisSpacing: 12, mainAxisSpacing: 12), delegate: SliverChildBuilderDelegate((context, index) {
        final items = [{'icon': Icons.gavel, 'title': 'الدستور'}, {'icon': Icons.work, 'title': 'قانون العمل'}, {'icon': Icons.family_restroom, 'title': 'الأحوال الشخصية'}, {'icon': Icons.school, 'title': 'قانون التعليم'}];
        final item = items[index];
        return Card(child: InkWell(onTap: () => context.push('/laws'), borderRadius: BorderRadius.circular(12), child: Column(mainAxisAlignment: MainAxisAlignment.center, children: [Icon(item['icon'] as IconData, size: 40, color: AppTheme.yemeniGreen), const SizedBox(height: 8), Text(item['title'] as String, style: const TextStyle(fontFamily: 'Cairo', fontWeight: FontWeight.bold), textAlign: TextAlign.center)])));
      }, childCount: 4)))),
      SliverToBoxAdapter(child: Padding(padding: const EdgeInsets.symmetric(horizontal: 16), child: Row(mainAxisAlignment: MainAxisAlignment.spaceBetween, children: [const Text('آخر القوانين', style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold)), TextButton(onPressed: () => context.push('/laws'), child: const Text('عرض الكل'))])),
      SliverList(delegate: SliverChildBuilderDelegate((context, index) => Card(margin: const EdgeInsets.symmetric(horizontal: 16, vertical: 8), child: ListTile(leading: CircleAvatar(backgroundColor: AppTheme.yemeniGreen.withOpacity(0.1), child: const Icon(Icons.article, color: AppTheme.yemeniGreen)), title: const Text('قانون العمل اليمني'), subtitle: const Text('آخر تحديث: 2024'), trailing: const Icon(Icons.arrow_forward_ios, size: 16), onTap: () => context.push('/law/1'))), childCount: 3)),
      const SliverToBoxAdapter(child: SizedBox(height: 16)),
    ]);
  }
}

class LawsTab extends StatelessWidget {
  const LawsTab({super.key});
  @override
  Widget build(BuildContext context) => const Center(child: Text('القوانين', style: TextStyle(fontSize: 20)));
}

class ConsultationsTab extends StatelessWidget {
  const ConsultationsTab({super.key});
  @override
  Widget build(BuildContext context) => const Center(child: Text('الاستشارات', style: TextStyle(fontSize: 20)));
}

class ProfileTab extends StatelessWidget {
  const ProfileTab({super.key});
  @override
  Widget build(BuildContext context) => const Center(child: Text('الملف الشخصي', style: TextStyle(fontSize: 20)));
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
    {'id': 'all', 'name': 'الكل', 'icon': Icons.library_books},
    {'id': 'constitution', 'name': 'الدستور', 'icon': Icons.gavel},
    {'id': 'labor', 'name': 'قانون العمل', 'icon': Icons.work},
    {'id': 'personal_status', 'name': 'الأحوال الشخصية', 'icon': Icons.family_restroom},
    {'id': 'education', 'name': 'قانون التعليم', 'icon': Icons.school},
  ];
  final List<Map<String, dynamic>> _laws = [
    {'id': '1', 'title': 'الدستور اليمني', 'category': 'constitution', 'articlesCount': 150, 'lastUpdate': '2024-01-15'},
    {'id': '2', 'title': 'قانون العمل اليمني', 'category': 'labor', 'articlesCount': 200, 'lastUpdate': '2024-02-20'},
    {'id': '3', 'title': 'قانون الأحوال الشخصية', 'category': 'personal_status', 'articlesCount': 180, 'lastUpdate': '2024-01-10'},
    {'id': '4', 'title': 'قانون التعليم', 'category': 'education', 'articlesCount': 120, 'lastUpdate': '2024-03-05'},
  ];
  List<Map<String, dynamic>> get _filteredLaws => _selectedCategory == 'all' ? _laws : _laws.where((law) => law['category'] == _selectedCategory).toList();

  @override
  Widget build(BuildContext context) {
    return Scaffold(appBar: AppBar(title: const Text('الموسوعة القانونية'), actions: [IconButton(icon: const Icon(Icons.search), onPressed: () => context.push('/search'))]), body: Column(children: [
      SizedBox(height: 100, child: ListView.builder(scrollDirection: Axis.horizontal, padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 8), itemCount: _categories.length, itemBuilder: (context, index) {
        final category = _categories[index];
        final isSelected = _selectedCategory == category['id'];
        return Padding(padding: const EdgeInsets.only(left: 8), child: FilterChip(label: Row(mainAxisSize: MainAxisSize.min, children: [Icon(category['icon'], size: 18), const SizedBox(width: 8), Text(category['name'])]), selected: isSelected, onSelected: (selected) => setState(() => _selectedCategory = category['id']), backgroundColor: Colors.grey.shade100, selectedColor: AppTheme.yemeniGreen.withOpacity(0.2)));
      })),
      const Divider(),
      Expanded(child: ListView.builder(padding: const EdgeInsets.all(16), itemCount: _filteredLaws.length, itemBuilder: (context, index) {
        final law = _filteredLaws[index];
        return Card(margin: const EdgeInsets.only(bottom: 12), child: ListTile(leading: CircleAvatar(backgroundColor: AppTheme.yemeniGreen.withOpacity(0.1), child: const Icon(Icons.article, color: AppTheme.yemeniGreen)), title: Text(law['title'], style: const TextStyle(fontFamily: 'Cairo', fontWeight: FontWeight.bold)), subtitle: Text('${law['articlesCount']} مادة - آخر تحديث: ${law['lastUpdate']}'), trailing: const Icon(Icons.arrow_forward_ios, size: 16), onTap: () => context.push('/law/${law['id']}')));
      })),
    ]));
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
    {'number': 1, 'title': 'المادة الأولى', 'content': 'الجمهورية اليمنية دولة عربية إسلامية مستقلة ذات سيادة تامة، وهي وحدة لا تتجزأ ولا يجوز التنازل عن أي جزء من أراضيها...'},
    {'number': 2, 'title': 'المادة الثانية', 'content': 'الإسلام دين الدولة، والشريعة الإسلامية مصدر جميع التشريعات...'},
    {'number': 3, 'title': 'المادة الثالثة', 'content': 'اللغة العربية هي اللغة الرسمية للدولة...'},
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(appBar: AppBar(title: const Text('الدستور اليمني'), actions: [IconButton(icon: Icon(_isFavorite ? Icons.favorite : Icons.favorite_border), onPressed: () => setState(() => _isFavorite = !_isFavorite)), IconButton(icon: const Icon(Icons.share), onPressed: () {})]), body: Expanded(child: ListView.builder(padding: const EdgeInsets.all(16), itemCount: _articles.length, itemBuilder: (context, index) {
      final article = _articles[index];
      return Card(margin: const EdgeInsets.only(bottom: 12), child: ExpansionTile(leading: CircleAvatar(backgroundColor: AppTheme.yemeniGreen, child: Text('${article['number']}', style: const TextStyle(color: Colors.white, fontWeight: FontWeight.bold))), title: Text(article['title'], style: const TextStyle(fontFamily: 'Cairo', fontWeight: FontWeight.bold)), subtitle: Text(article['content'].substring(0, 50) + '...', maxLines: 1, overflow: TextOverflow.ellipsis), children: [Padding(padding: const EdgeInsets.all(16), child: Text(article['content'], style: const TextStyle(fontFamily: 'Cairo', fontSize: 16, height: 1.8)))]));
    })));
  }
}
""")

write_file(f"{base_dir}/lib/features/laws/screens/search_screen.dart", """import 'package:flutter/material.dart';
import '../../../core/config/theme/app_theme.dart';

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
    {'id': '1', 'title': 'الدستور اليمني', 'category': 'الدستور'},
    {'id': '2', 'title': 'قانون العمل', 'category': 'العمل'},
    {'id': '3', 'title': 'قانون الأحوال الشخصية', 'category': 'الأحوال الشخصية'},
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
    return Scaffold(appBar: AppBar(title: const Text('البحث في القوانين')), body: Column(children: [
      Padding(padding: const EdgeInsets.all(16), child: TextField(controller: _searchController, decoration: InputDecoration(hintText: 'ابحث عن قانون أو مادة...', prefixIcon: const Icon(Icons.search), suffixIcon: _searchController.text.isNotEmpty ? IconButton(icon: const Icon(Icons.clear), onPressed: () { _searchController.clear(); _search(''); }) : null, border: OutlineInputBorder(borderRadius: BorderRadius.circular(12))), onChanged: _search)),
      if (_isSearching) const Expanded(child: Center(child: CircularProgressIndicator()))
      else if (_searchResults.isEmpty && _searchController.text.isNotEmpty)
        Expanded(child: Center(child: Column(mainAxisAlignment: MainAxisAlignment.center, children: [Icon(Icons.search_off, size: 80, color: Colors.grey.shade400), const SizedBox(height: 16), const Text('لا توجد نتائج', style: TextStyle(fontSize: 18, color: Colors.grey))])))
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
    {'id': '1', 'title': 'استشارة حول عقد عمل', 'lawyerName': 'أحمد محمد علي', 'status': 'in_progress', 'date': '2024-06-25', 'lastMessage': 'شكراً لك، سأراجع العقد وأعود إليك'},
    {'id': '2', 'title': 'قضية طلاق', 'lawyerName': 'فاطمة أحمد', 'status': 'completed', 'date': '2024-06-20', 'lastMessage': 'تم الانتهاء من القضية بنجاح'},
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
      case 'pending': return 'قيد الانتظار';
      case 'in_progress': return 'قيد المعالجة';
      case 'completed': return 'مكتملة';
      case 'cancelled': return 'ملغاة';
      default: return status;
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(appBar: AppBar(title: const Text('استشاراتي'), bottom: TabBar(controller: _tabController, tabs: const [Tab(text: 'الكل'), Tab(text: 'قيد المعالجة'), Tab(text: 'المكتملة')])), body: TabBarView(controller: _tabController, children: [_buildConsultationsList(_consultations), _buildConsultationsList(_consultations.where((c) => c['status'] == 'in_progress').toList()), _buildConsultationsList(_consultations.where((c) => c['status'] == 'completed').toList())]), floatingActionButton: FloatingActionButton.extended(onPressed: () => context.push('/new-consultation'), icon: const Icon(Icons.add), label: const Text('استشارة جديدة')));
  }

  Widget _buildConsultationsList(List<Map<String, dynamic>> consultations) {
    if (consultations.isEmpty) return const Center(child: Column(mainAxisAlignment: MainAxisAlignment.center, children: [Icon(Icons.chat_bubble_outline, size: 80, color: Colors.grey), SizedBox(height: 16), Text('لا توجد استشارات', style: TextStyle(fontSize: 18, color: Colors.grey))]));
    return ListView.builder(padding: const EdgeInsets.all(16), itemCount: consultations.length, itemBuilder: (context, index) {
      final consultation = consultations[index];
      return Card(margin: const EdgeInsets.only(bottom: 12), child: ListTile(leading: CircleAvatar(backgroundColor: AppTheme.yemeniGreen.withOpacity(0.1), child: const Icon(Icons.person, color: AppTheme.yemeniGreen)), title: Text(consultation['title'], style: const TextStyle(fontWeight: FontWeight.bold)), subtitle: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [const SizedBox(height: 4), Text(consultation['lawyerName']), const SizedBox(height: 4), Text(consultation['lastMessage'], maxLines: 1, overflow: TextOverflow.ellipsis)]), trailing: Column(mainAxisAlignment: MainAxisAlignment.center, crossAxisAlignment: CrossAxisAlignment.end, children: [Container(padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 4), decoration: BoxDecoration(color: _getStatusColor(consultation['status']).withOpacity(0.1), borderRadius: BorderRadius.circular(12)), child: Text(_getStatusText(consultation['status']), style: TextStyle(color: _getStatusColor(consultation['status']), fontSize: 12, fontWeight: FontWeight.bold))), const SizedBox(height: 4), Text(consultation['date'], style: TextStyle(fontSize: 12, color: Colors.grey.shade600))]), onTap: () => context.push('/consultation/${consultation['id']}')));
    });
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
    {'id': '1', 'senderId': 'client', 'content': 'مرحباً، لدي استفسار حول عقد العمل', 'time': '10:30 ص'},
    {'id': '2', 'senderId': 'lawyer', 'content': 'أهلاً بك، تفضل بطرح استفسارك', 'time': '10:35 ص'},
    {'id': '3', 'senderId': 'client', 'content': 'هل يمكن لصاحب العمل إنهاء العقد دون تعويض؟', 'time': '10:40 ص'},
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
      _messages.add({'id': DateTime.now().millisecondsSinceEpoch.toString(), 'senderId': 'client', 'content': _messageController.text, 'time': '${DateTime.now().hour}:${DateTime.now().minute}'});
    });
    _messageController.clear();
    Future.delayed(const Duration(milliseconds: 100), () => _scrollController.animateTo(_scrollController.position.maxScrollExtent, duration: const Duration(milliseconds: 300), curve: Curves.easeOut));
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(appBar: AppBar(title: const Column(crossAxisAlignment: CrossAxisAlignment.start, children: [Text('استشارة حول عقد عمل'), Text('أحمد محمد علي', style: TextStyle(fontSize: 12, fontWeight: FontWeight.normal))]), actions: [IconButton(icon: const Icon(Icons.attach_file), onPressed: () {}), IconButton(icon: const Icon(Icons.more_vert), onPressed: () {})]), body: Column(children: [
      Expanded(child: ListView.builder(controller: _scrollController, padding: const EdgeInsets.all(16), itemCount: _messages.length, itemBuilder: (context, index) {
        final message = _messages[index];
        final isMe = message['senderId'] == 'client';
        return Align(alignment: isMe ? Alignment.centerLeft : Alignment.centerRight, child: Container(margin: const EdgeInsets.only(bottom: 12), padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 10), decoration: BoxDecoration(color: isMe ? AppTheme.yemeniGreen : Colors.grey.shade200, borderRadius: BorderRadius.only(topLeft: const Radius.circular(12), topRight: const Radius.circular(12), bottomLeft: Radius.circular(isMe ? 12 : 0), bottomRight: Radius.circular(isMe ? 0 : 12))), child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [Text(message['content'], style: TextStyle(color: isMe ? Colors.white : Colors.black)), const SizedBox(height: 4), Text(message['time'], style: TextStyle(fontSize: 10, color: isMe ? Colors.white70 : Colors.black54))])));
      })),
      Container(padding: const EdgeInsets.all(16), decoration: BoxDecoration(color: Colors.white, boxShadow: [BoxShadow(color: Colors.black.withOpacity(0.1), blurRadius: 4, offset: const Offset(0, -2))]), child: Row(children: [Expanded(child: TextField(controller: _messageController, decoration: InputDecoration(hintText: 'اكتب رسالتك...', border: OutlineInputBorder(borderRadius: BorderRadius.circular(24)), contentPadding: const EdgeInsets.symmetric(horizontal: 20, vertical: 12)), maxLines: null, textInputAction: TextInputAction.send, onSubmitted: (_) => _sendMessage())), const SizedBox(width: 8), CircleAvatar(backgroundColor: AppTheme.yemeniGreen, child: IconButton(icon: const Icon(Icons.send, color: Colors.white), onPressed: _sendMessage))])),
    ]));
  }
}
""")

write_file(f"{base_dir}/lib/features/consultations/screens/new_consultation_screen.dart", """import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import '../../../core/config/theme/app_theme.dart';

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
  final List<String> _categories = ['قانون العمل', 'الأحوال الشخصية', 'القانون الجنائي', 'القانون المدني', 'قانون التعليم', 'أخرى'];

  @override
  void dispose() {
    _titleController.dispose();
    _descriptionController.dispose();
    super.dispose();
  }

  void _submitConsultation() {
    if (!_formKey.currentState!.validate()) return;
    showDialog(context: context, builder: (context) => AlertDialog(title: const Text('تم إرسال الاستشارة'), content: const Text('سيتم مراجعة استشارتك والرد عليك في أقرب وقت'), actions: [TextButton(onPressed: () { Navigator.pop(context); context.pop(); }, child: const Text('حسناً'))]));
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(appBar: AppBar(title: const Text('استشارة جديدة')), body: SingleChildScrollView(padding: const EdgeInsets.all(24), child: Form(key: _formKey, child: Column(crossAxisAlignment: CrossAxisAlignment.stretch, children: [
      TextFormField(controller: _titleController, decoration: const InputDecoration(labelText: 'عنوان الاستشارة', hintText: 'مثال: استفسار حول عقد العمل'), validator: (value) => value == null || value.isEmpty ? 'الرجاء إدخال عنوان الاستشارة' : null),
      const SizedBox(height: 16),
      DropdownButtonFormField<String>(decoration: const InputDecoration(labelText: 'التصنيف'), value: _selectedCategory.isEmpty ? null : _selectedCategory, items: _categories.map((category) => DropdownMenuItem(value: category, child: Text(category))).toList(), onChanged: (value) => setState(() => _selectedCategory = value!), validator: (value) => value == null || value.isEmpty ? 'الرجاء اختيار تصنيف' : null),
      const SizedBox(height: 16),
      TextFormField(controller: _descriptionController, decoration: const InputDecoration(labelText: 'تفاصيل الاستشارة', hintText: 'اشرح استفسارك بالتفصيل...'), maxLines: 6, validator: (value) => value == null || value.isEmpty ? 'الرجاء إدخال تفاصيل الاستشارة' : null),
      const SizedBox(height: 24),
      Card(child: ListTile(leading: const Icon(Icons.attach_file), title: const Text('إرفاق ملفات'), subtitle: const Text('PDF, Images, Documents'), trailing: const Icon(Icons.arrow_forward_ios, size: 16), onTap: () {})),
      const SizedBox(height: 24),
      ElevatedButton.icon(onPressed: _submitConsultation, icon: const Icon(Icons.send), label: const Text('إرسال الاستشارة'), style: ElevatedButton.styleFrom(padding: const EdgeInsets.symmetric(vertical: 16))),
    ])));
  }
}
""")

write_file(f"{base_dir}/lib/features/profile/screens/profile_screen.dart", """import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:go_router/go_router.dart';
import '../../../providers/auth_provider.dart';
import '../../../core/config/theme/app_theme.dart';

class ProfileScreen extends ConsumerWidget {
  const ProfileScreen({super.key});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final authState = ref.watch(authProvider);
    final userData = authState.userData;
    return Scaffold(appBar: AppBar(title: const Text('ملفي الشخصي'), actions: [IconButton(icon: const Icon(Icons.settings), onPressed: () {})]), body: SingleChildScrollView(child: Column(children: [
      const SizedBox(height: 24),
      CircleAvatar(radius: 60, backgroundColor: AppTheme.yemeniGreen.withOpacity(0.1), child: userData?['profileImage'] != null ? ClipOval(child: Image.network(userData!['profileImage'], fit: BoxFit.cover)) : const Icon(Icons.person, size: 60, color: AppTheme.yemeniGreen)),
      const SizedBox(height: 16),
      Text(userData?['fullName'] ?? 'مستخدم', style: const TextStyle(fontFamily: 'Cairo', fontSize: 24, fontWeight: FontWeight.bold)),
      Text(userData?['userType'] == 'lawyer' ? 'محامٍ' : 'مواطن', style: TextStyle(color: Colors.grey.shade600)),
      const SizedBox(height: 24),
      _buildMenuItem(context, icon: Icons.person_outline, title: 'تعديل الملف الشخصي', onTap: () => context.push('/edit-profile')),
      _buildMenuItem(context, icon: Icons.chat_bubble_outline, title: 'استشاراتي', onTap: () => context.push('/consultations')),
      _buildMenuItem(context, icon: Icons.bookmark_border, title: 'المحفوظات', onTap: () {}),
      _buildMenuItem(context, icon: Icons.help_outline, title: 'الأسئلة الشائعة', onTap: () => context.push('/faq')),
      _buildMenuItem(context, icon: Icons.info_outline, title: 'من نحن', onTap: () => context.push('/about')),
      _buildMenuItem(context, icon: Icons.privacy_tip_outlined, title: 'الخصوصية والشروط', onTap: () => context.push('/privacy')),
      const Divider(height: 32),
      ListTile(leading: const Icon(Icons.logout, color: AppTheme.yemeniRed), title: const Text('تسجيل الخروج', style: TextStyle(color: AppTheme.yemeniRed)), onTap: () => _showLogoutDialog(context, ref)),
      const SizedBox(height: 24),
    ])));
  }

  Widget _buildMenuItem(BuildContext context, {required IconData icon, required String title, required VoidCallback onTap}) {
    return Card(margin: const EdgeInsets.symmetric(horizontal: 16, vertical: 4), child: ListTile(leading: Icon(icon, color: AppTheme.yemeniGreen), title: Text(title, style: const TextStyle(fontFamily: 'Cairo')), trailing: const Icon(Icons.arrow_forward_ios, size: 16), onTap: onTap));
  }

  void _showLogoutDialog(BuildContext context, WidgetRef ref) {
    showDialog(context: context, builder: (context) => AlertDialog(title: const Text('تسجيل الخروج'), content: const Text('هل أنت متأكد من تسجيل الخروج؟'), actions: [TextButton(onPressed: () => Navigator.pop(context), child: const Text('إلغاء')), ElevatedButton(onPressed: () { ref.read(authProvider).signOut(); Navigator.pop(context); context.go('/login'); }, style: ElevatedButton.styleFrom(backgroundColor: AppTheme.yemeniRed), child: const Text('خروج'))]));
  }
}
""")

write_file(f"{base_dir}/lib/features/profile/screens/edit_profile_screen.dart", """import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:go_router/go_router.dart';
import 'package:image_picker/image_picker.dart';
import '../../../providers/auth_provider.dart';
import '../../../core/config/theme/app_theme.dart';

class EditProfileScreen extends ConsumerStatefulWidget {
  const EditProfileScreen({super.key});
  @override
  ConsumerState<EditProfileScreen> createState() => _EditProfileScreenState();
}

class _EditProfileScreenState extends ConsumerState<EditProfileScreen> {
  final _formKey = GlobalKey<FormState>();
  final _fullNameController = TextEditingController();
  final _emailController = TextEditingController();
  final _phoneController = TextEditingController();

  @override
  void initState() {
    super.initState();
    final userData = ref.read(authProvider).userData;
    _fullNameController.text = userData?['fullName'] ?? '';
    _emailController.text = userData?['email'] ?? '';
    _phoneController.text = userData?['phoneNumber'] ?? '';
  }

  @override
  void dispose() {
    _fullNameController.dispose();
    _emailController.dispose();
    _phoneController.dispose();
    super.dispose();
  }

  Future<void> _pickImage() async {
    final picker = ImagePicker();
    final pickedFile = await picker.pickImage(source: ImageSource.gallery);
    if (pickedFile != null) {
      setState(() {});
    }
  }

  Future<void> _saveProfile() async {
    if (!_formKey.currentState!.validate()) return;
    await ref.read(authProvider).updateProfile({'fullName': _fullNameController.text.trim(), 'phoneNumber': _phoneController.text.trim()});
    if (mounted) {
      ScaffoldMessenger.of(context).showSnackBar(const SnackBar(content: Text('تم حفظ التغييرات بنجاح'), backgroundColor: AppTheme.yemeniGreen));
      context.pop();
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(appBar: AppBar(title: const Text('تعديل الملف الشخصي')), body: SingleChildScrollView(padding: const EdgeInsets.all(24), child: Form(key: _formKey, child: Column(children: [
      Stack(children: [
        CircleAvatar(radius: 60, backgroundColor: AppTheme.yemeniGreen.withOpacity(0.1), child: const Icon(Icons.person, size: 60, color: AppTheme.yemeniGreen)),
        Positioned(bottom: 0, right: 0, child: CircleAvatar(backgroundColor: AppTheme.yemeniGreen, child: IconButton(icon: const Icon(Icons.camera_alt, color: Colors.white, size: 20), onPressed: _pickImage))),
      ]),
      const SizedBox(height: 32),
      TextFormField(controller: _fullNameController, decoration: const InputDecoration(labelText: 'الاسم الكامل', prefixIcon: Icon(Icons.person_outline)), validator: (value) => value == null || value.isEmpty ? 'الرجاء إدخال الاسم' : null),
      const SizedBox(height: 16),
      TextFormField(controller: _emailController, decoration: const InputDecoration(labelText: 'البريد الإلكتروني', prefixIcon: Icon(Icons.email_outlined)), enabled: false),
      const SizedBox(height: 16),
      TextFormField(controller: _phoneController, decoration: const InputDecoration(labelText: 'رقم الهاتف', prefixIcon: Icon(Icons.phone_outlined)), validator: (value) => value == null || value.isEmpty ? 'الرجاء إدخال رقم الهاتف' : null),
      const SizedBox(height: 32),
      ElevatedButton.icon(onPressed: _saveProfile, icon: const Icon(Icons.save), label: const Text('حفظ التغييرات'), style: ElevatedButton.styleFrom(padding: const EdgeInsets.symmetric(horizontal: 48, vertical: 16))),
    ])));
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
    {'id': '1', 'clientName': 'محمد عبدالله', 'title': 'استشارة حول فصل تعسفي', 'date': 'منذ 5 دقائق'},
    {'id': '2', 'clientName': 'سارة أحمد', 'title': 'قضية حضانة أطفال', 'date': 'منذ ساعة'},
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(appBar: AppBar(title: const Text('لوحة تحكم المحامي')), body: SingleChildScrollView(padding: const EdgeInsets.all(16), child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
      Row(children: [
        Expanded(child: _buildStatCard('الطلبات الجديدة', '12', Icons.pending_actions, Colors.orange)),
        const SizedBox(width: 12),
        Expanded(child: _buildStatCard('قيد المعالجة', '5', Icons.hourglass_bottom, Colors.blue)),
        const SizedBox(width: 12),
        Expanded(child: _buildStatCard('مكتملة', '48', Icons.check_circle, Colors.green)),
      ]),
      const SizedBox(height: 24),
      const Text('طلبات الاستشارة الواردة', style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold)),
      const SizedBox(height: 12),
      ListView.builder(shrinkWrap: true, physics: const NeverScrollableScrollPhysics(), itemCount: _pendingRequests.length, itemBuilder: (context, index) {
        final req = _pendingRequests[index];
        return Card(margin: const EdgeInsets.only(bottom: 12), child: Padding(padding: const EdgeInsets.all(16), child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
          Row(mainAxisAlignment: MainAxisAlignment.spaceBetween, children: [Text(req['clientName'], style: const TextStyle(fontWeight: FontWeight.bold, fontSize: 16)), Text(req['date'], style: TextStyle(color: Colors.grey.shade600, fontSize: 12))]),
          const SizedBox(height: 8),
          Text(req['title']),
          const SizedBox(height: 16),
          Row(children: [Expanded(child: OutlinedButton(onPressed: () {}, child: const Text('رفض'))), const SizedBox(width: 12), Expanded(child: ElevatedButton(onPressed: () => context.push('/consultation/${req['id']}'), child: const Text('قبول والرد')))]),
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
    return Scaffold(appBar: AppBar(title: const Text('الملف المهني')), body: SingleChildScrollView(child: Column(children: [
      const SizedBox(height: 24),
      const CircleAvatar(radius: 50, backgroundColor: AppTheme.yemeniGreen, child: Icon(Icons.person, size: 50, color: Colors.white)),
      const SizedBox(height: 16),
      const Text('أ. أحمد محمد علي', style: TextStyle(fontSize: 22, fontWeight: FontWeight.bold)),
      const Text('محامٍ ومستشار قانوني', style: TextStyle(color: Colors.grey)),
      const SizedBox(height: 8),
      Row(mainAxisAlignment: MainAxisAlignment.center, children: [const Icon(Icons.star, color: Colors.amber, size: 20), const SizedBox(width: 4), const Text('4.8', style: TextStyle(fontWeight: FontWeight.bold)), const SizedBox(width: 16), const Icon(Icons.work_outline, size: 20), const SizedBox(width: 4), const Text('10 سنوات خبرة')]),
      const SizedBox(height: 24),
      Padding(padding: const EdgeInsets.symmetric(horizontal: 24), child: Card(child: Padding(padding: const EdgeInsets.all(16), child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
        const Text('التخصصات', style: TextStyle(fontWeight: FontWeight.bold, fontSize: 16)),
        const SizedBox(height: 8),
        Wrap(spacing: 8, runSpacing: 8, children: [_buildChip('قانون العمل'), _buildChip('الأحوال الشخصية'), _buildChip('القانون التجاري')]),
        const SizedBox(height: 16),
        const Text('نبذة مهنية', style: TextStyle(fontWeight: FontWeight.bold, fontSize: 16)),
        const SizedBox(height: 8),
        const Text('محامٍ مرخص لدى نقابة المحامين اليمنيين، متخصص في قضايا العمل والأحوال الشخصية بخبرة تزيد عن 10 سنوات.'),
      ])))),
      const SizedBox(height: 24),
      Padding(padding: const EdgeInsets.symmetric(horizontal: 24), child: SizedBox(width: double.infinity, child: ElevatedButton.icon(onPressed: () => context.push('/new-consultation'), icon: const Icon(Icons.chat), label: const Text('طلب استشارة'), style: ElevatedButton.styleFrom(padding: const EdgeInsets.symmetric(vertical: 16))))),
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
    return Scaffold(appBar: AppBar(title: const Text('من نحن')), body: SingleChildScrollView(padding: const EdgeInsets.all(24), child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
      Center(child: Icon(Icons.balance, size: 80, color: AppTheme.yemeniGreen)),
      const SizedBox(height: 24),
      const Text('حقي كيمني', style: TextStyle(fontSize: 28, fontWeight: FontWeight.bold, textAlign: TextAlign.center)),
      const SizedBox(height: 8),
      const Text('موسوعتك القانونية الشاملة', style: TextStyle(fontSize: 16, color: Colors.grey), textAlign: TextAlign.center),
      const SizedBox(height: 32),
      _buildSection('رؤيتنا', 'أن نكون المرجع القانوني الأول لكل مواطن يمني، ونشر الوعي الحقوقي في المجتمع.'),
      const SizedBox(height: 16),
      _buildSection('رسالتنا', 'توفير المعلومات القانونية الموثوقة والمبسطة، وربط المواطنين بمحامين متخصصين لضمان حصول الجميع على حقوقهم.'),
      const SizedBox(height: 16),
      _buildSection('أهدافنا', ['نشر الثقافة القانونية بين أفراد المجتمع.', 'توفير قاعدة بيانات شاملة للقوانين اليمنية.', 'تسهيل الوصول إلى الاستشارات القانونية.', 'دعم الفئات الأكثر احتياجاً للمعرفة القانونية.']),
      const SizedBox(height: 32),
      const Center(child: Text('الإصدار 1.0.0\\nجميع الحقوق محفوظة © 2024', textAlign: TextAlign.center, style: TextStyle(color: Colors.grey))),
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
    return Scaffold(appBar: AppBar(title: const Text('سياسة الخصوصية')), body: SingleChildScrollView(padding: const EdgeInsets.all(24), child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
      _buildHeading('مقدمة'),
      _buildText('نرحب بك في تطبيق "حقي كيمني". نحن نلتزم بحماية خصوصيتك وبياناتك الشخصية. توضح سياسة الخصوصية هذه كيفية جمعنا واستخدامنا وحمايتنا لمعلوماتك.'),
      const SizedBox(height: 24),
      _buildHeading('المعلومات التي نجمعها'),
      _buildText('نقوم بجمع المعلومات التي تقدمها لنا عند التسجيل، مثل: الاسم، البريد الإلكتروني، رقم الهاتف. كما قد نجمع معلومات حول استخدامك للتطبيق لتحسين خدماتنا.'),
      const SizedBox(height: 24),
      _buildHeading('كيف نستخدم معلوماتك'),
      _buildList(['توفير خدمات الاستشارات القانونية.', 'التواصل معك بشأن استفساراتك.', 'تحسين وتطوير التطبيق.', 'إرسال إشعارات هامة (بموافقتك).']),
      const SizedBox(height: 24),
      _buildHeading('أمان البيانات'),
      _buildText('نستخدم تقنيات تشفير متقدمة لحماية بياناتك. لا نقوم بمشاركة معلوماتك الشخصية مع أطراف ثالثة إلا بموافقتك أو عند الطلب القانوني.'),
      const SizedBox(height: 24),
      _buildHeading('التواصل معنا'),
      _buildText('لأي استفسارات حول سياسة الخصوصية، يرجى التواصل معنا عبر البريد الإلكتروني: privacy@myyemeniright.com'),
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
    return Scaffold(appBar: AppBar(title: const Text('شروط الاستخدام')), body: SingleChildScrollView(padding: const EdgeInsets.all(24), child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
      const Text('شروط وأحكام الاستخدام', style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold)),
      const SizedBox(height: 24),
      _buildSection('1. قبول الشروط', 'باستخدامك لتطبيق "حقي كيمني"، فإنك توافق على الالتزام بهذه الشروط والأحكام. إذا لم توافق على أي جزء منها، يرجى عدم استخدام التطبيق.'),
      const SizedBox(height: 16),
      _buildSection('2. طبيعة الخدمة', 'يوفر التطبيق معلومات قانونية عامة واستشارات عبر محامين مرخصين. المعلومات المقدمة لا تغني عن الاستشارة القانونية المباشرة في القضايا المعقدة.'),
      const SizedBox(height: 16),
      _buildSection('3. حسابات المستخدمين', 'أنت مسؤول عن الحفاظ على سرية بيانات حسابك. يجب أن تكون المعلومات المقدمة عند التسجيل دقيقة وحديثة.'),
      const SizedBox(height: 16),
      _buildSection('4. الملكية الفكرية', 'جميع المحتويات القانونية والشعارات والتصاميم داخل التطبيق محمية بموجب حقوق الملكية الفكرية ولا يجوز نسخها دون إذن.'),
      const SizedBox(height: 16),
      _buildSection('5. إخلاء المسؤولية', 'التطبيق لا يتحمل مسؤولية أي قرارات يتخذها المستخدم بناءً على المعلومات الموجودة في التطبيق دون الرجوع إلى محامٍ مختص.'),
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
    {'q': 'كم مدة إجازة الوضع للمرأة العاملة في اليمن؟', 'a': 'وفقاً لقانون العمل اليمني، تستحق المرأة العاملة إجازة وضع مدفوعة الأجر لمدة (60) يوماً، توزع قبل الولادة وبعدها وفقاً للحالة الصحية.'},
    {'q': 'ما هي حقوق المرأة في الميراث؟', 'a': 'كفل القانون اليمني والشريعة الإسلامية للمرأة حقها في الميراث. للمرأة نصف ما للرجل في حالات معينة، ولها كامل الحق في التركة في حالات أخرى وفقاً لنظام القرابة.'},
    {'q': 'هل يحق لصاحب العمل فصل العامل دون سبب؟', 'a': 'لا، لا يجوز فصل العامل تعسفياً. إذا تم الفصل دون سبب مشروع، يحق للعامل المطالبة بتعويض وفقاً لأحكام قانون العمل اليمني.'},
    {'q': 'ما هي سن الحضانة للأم في اليمن؟', 'a': 'تمنح الحضانة للأم حتى يبلغ الطفل سن السابعة للذكر والتاسعة للأنثى، ويمكن للقاضي تمديدها لما فيه مصلحة المحضون.'},
    {'q': 'ما هي حقوق ذوي الإعاقة في التعليم؟', 'a': 'يكفل القانون اليمني حق ذوي الإعاقة في التعليم المجاني والإلزامي، مع توفير البيئة المناسبة ودمجهم في المدارس الحكومية.'},
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(appBar: AppBar(title: const Text('الأسئلة الشائعة')), body: ListView.builder(padding: const EdgeInsets.all(16), itemCount: _faqs.length, itemBuilder: (context, index) {
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
        classpath "org.jetbrains.kotlin:kotlin-gradle-plugin:$kotlin_version"
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
    project.buildDir = "${rootProject.buildDir}/${project.name}"
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
        android:label="حقي كيمني"
        android:name="${applicationName}"
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

    includeBuild("${settings.ext.flutterSdkPath}/packages/flutter_tools/gradle")

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

write_file(f"{base_dir}/README.md", """# حقي كيمني - My Yemeni Right
التطبيق القانوني الشامل للمواطن اليمني

## المتطلبات
- Flutter 3.10+
- Dart 3.0+
- Android Studio أو VS Code

## خطوات البناء
1. تثبيت المكتبات
```bash
flutter pub get
