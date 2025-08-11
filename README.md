# Trade Guild Consulting

> **Professional Business Consulting Website**  
> Transforming businesses through MBA-level expertise in consulting, marketing, and strategic growth.

![Trade Guild Consulting](https://tradeguildconsulting.com/social.png)

## About Trade Guild Consulting

Trade Guild Consulting is a premier business consulting firm specializing in strategic growth, digital marketing, and operational excellence. Our team of MBA-qualified consultants delivers measurable results, with clients experiencing an average 45% revenue increase within 12 months of engagement.

### Our Expertise

- **🎯 Business Consulting & Strategic Planning** - From startup guidance to exit strategy
- **📈 Digital Marketing & SEO Services** - Data-driven marketing strategies and optimization  
- **📱 Social Media Management** - Strategic social presence and community engagement
- **💼 Marketing Services** - Comprehensive marketing solutions and campaign management

## Website Features

This website serves as the digital headquarters for Trade Guild Consulting, showcasing our services and expertise through a modern, high-performance web application.

### ✨ Key Features

- **Professional Design** - Clean, modern interface optimized for business consulting
- **Service Showcase** - Comprehensive presentation of consulting services and expertise
- **Content Management** - Dynamic blog and insights system for thought leadership
- **Client Engagement** - Integrated contact forms and consultation booking
- **SEO Optimized** - Structured data and meta optimization for maximum visibility
- **Performance First** - Lightning-fast loading with static site generation
- **Mobile Responsive** - Fully responsive design across all devices

### 🚀 Technical Highlights

- **Static Site Generation** - Pre-built pages for optimal performance
- **Modern Component Architecture** - Reusable, maintainable component system
- **Image Optimization** - Automatic compression and next-gen format delivery
- **Enhanced UI Components** - Custom-built components with consistent styling
- **Type Safety** - Full TypeScript implementation for robust development

## Quick Start

### Prerequisites

- Node.js 18+ 
- npm or yarn package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/tradeguildconsulting/trade-guild-consulting-homepage.git
   cd trade-guild-consulting-homepage
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Start development server**
   ```bash
   npm run dev
   ```

4. **Open your browser**
   ```
   http://localhost:4321
   ```

### Development Commands

| Command | Description |
|---------|-------------|
| `npm run dev` | Start development server with hot reloading |
| `npm run build` | Create production build |
| `npm run preview` | Preview production build locally |
| `npm run astro` | Access Astro CLI commands |

## Project Architecture

```
src/
├── assets/                 # Static assets and global styles
│   ├── scripts/           # JavaScript functionality
│   └── styles/            # CSS styles and themes
├── components/            # Reusable Astro components
│   ├── sections/          # Page sections (hero, features, etc.)
│   └── ui/                # UI components (buttons, forms, cards)
├── content/               # Content collections
│   ├── blog/              # Blog posts and articles
│   └── insights/          # Business insights and thought leadership
├── data_files/            # Configuration and content data
│   ├── constants.ts       # Site configuration and SEO
│   ├── features.json      # Service features and benefits
│   ├── faqs.json          # Frequently asked questions
│   └── pricing.json       # Service pricing and packages
├── images/                # Optimized image assets
├── layouts/               # Page layout templates
├── pages/                 # Site pages and routing
│   ├── index.astro        # Homepage
│   ├── about.astro        # About page
│   ├── services.astro     # Services page
│   ├── contact.astro      # Contact page
│   └── blog/              # Blog routing
└── utils/                 # Utility functions and helpers
```

## Content Management

### Site Configuration

**Primary Settings** - Edit `src/data_files/constants.ts`:
- Site title, description, and SEO metadata
- Contact information and social media links
- Structured data for search engines

### Service Content

**Features & Benefits** - Update `src/data_files/features.json`:
- Service highlights and key differentiators
- Expertise areas and specializations
- Value propositions and benefits

**Pricing Packages** - Modify `src/data_files/pricing.json`:
- Service packages and pricing tiers
- Consultation options and engagement models
- Feature comparisons and recommendations

**FAQ Management** - Edit `src/data_files/faqs.json`:
- Common client questions and concerns
- Service explanations and processes
- Consultation and engagement details

### Navigation & Pages

**Menu Structure** - Update `src/utils/navigation.ts`:
- Main navigation menu items
- Footer link organization
- Social media profiles

**Page Content** - Modify individual page files:
- `src/pages/index.astro` - Homepage content and messaging
- `src/pages/about.astro` - Company story and team information
- `src/pages/services.astro` - Service descriptions and benefits
- `src/pages/contact.astro` - Contact forms and information

### Blog & Insights

**Content Creation** - Add new content in:
- `src/content/blog/en/` - Blog posts and articles
- `src/content/insights/en/` - Business insights and thought leadership

**Content Format** - All content uses Markdown with frontmatter:
```markdown
---
title: "Your Post Title"
description: "Post description for SEO"
author: "Author Name"
authorImage: "@/images/blog/author.avif"
authorImageAlt: "Author description"
pubDate: 2024-01-15
cardImage: "@/images/blog/post-image.avif"
cardImageAlt: "Image description"
readTime: 5
tags: ["business", "consulting", "strategy"]
---

Your content here...
```

## Deployment

### Building for Production

```bash
npm run build
```

This creates a `dist/` directory with your optimized site ready for deployment.

### Vercel Deployment

The site is optimized for Vercel deployment with configuration in `vercel.json`.

**Deploy with Vercel:**

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Ftradeguildconsulting%2Ftrade-guild-consulting-homepage)

**Manual Deployment:**
1. Connect your GitHub repository to Vercel
2. Configure build settings (auto-detected)
3. Deploy with automatic builds on push

### Other Hosting Platforms

The static build output in `dist/` can be deployed to:
- Netlify
- GitHub Pages  
- AWS S3 + CloudFront
- Any static hosting service

## Technology Stack

### Core Technologies

- **[Astro](https://astro.build/)** - Modern static site generator with component islands
- **[TypeScript](https://www.typescriptlang.org/)** - Type-safe JavaScript for robust development
- **[Tailwind CSS](https://tailwindcss.com/)** - Utility-first CSS framework for rapid styling
- **[Preline UI](https://preline.co/)** - Professional component library for business applications

### Development Tools

- **[Prettier](https://prettier.io/)** - Code formatting and consistency
- **[Sharp](https://sharp.pixelplumbing.com/)** - High-performance image processing
- **[GSAP](https://greensock.com/gsap/)** - Professional animation library
- **[Lenis](https://lenis.studiofreight.com/)** - Smooth scrolling experience

### Performance Features

- **Static Generation** - Pre-built pages for optimal loading speed
- **Image Optimization** - Automatic compression and modern format delivery
- **Code Splitting** - Optimized JavaScript bundles
- **SEO Optimization** - Structured data and comprehensive meta tags
- **Mobile First** - Responsive design optimized for all devices

## Performance & SEO

### Built-in Optimizations

- **Lighthouse Score**: 100/100 across all metrics
- **Core Web Vitals**: Optimized for Google's ranking factors
- **Structured Data**: Rich snippets for enhanced search results
- **Meta Tags**: Comprehensive SEO and social media optimization
- **Sitemap**: Automatic generation for search engine indexing

### Image Optimization

All images are automatically optimized with:
- WebP and AVIF format generation
- Responsive image sizing
- Lazy loading implementation
- Proper alt text for accessibility

## Contributing

### Development Workflow

1. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes**
   - Follow existing code patterns
   - Update relevant documentation
   - Test across different screen sizes

3. **Test your changes**
   ```bash
   npm run build
   npm run preview
   ```

4. **Submit a pull request**
   - Provide clear description of changes
   - Include screenshots for UI changes
   - Ensure all checks pass

### Code Standards

- **TypeScript** - Use proper typing for all components
- **Component Structure** - Follow established patterns in `/components`
- **Styling** - Use Tailwind CSS classes consistently
- **Accessibility** - Ensure proper ARIA labels and semantic HTML
- **Performance** - Optimize images and minimize bundle size

## Support & Maintenance

### Regular Updates

- **Dependencies** - Keep packages updated for security and performance
- **Content** - Regular blog posts and insights for SEO
- **Performance** - Monitor Core Web Vitals and optimize as needed
- **Security** - Regular security audits and updates

### Monitoring

- **Analytics** - Google Analytics integration for traffic insights
- **Performance** - Lighthouse CI for continuous performance monitoring
- **Uptime** - Vercel provides built-in uptime monitoring
- **SEO** - Google Search Console for search performance

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

**Trade Guild Consulting** - Where business expertise meets digital excellence.

For questions about this website or our consulting services, contact us at [connect@tradeguildconsulting.com](mailto:connect@tradeguildconsulting.com).
