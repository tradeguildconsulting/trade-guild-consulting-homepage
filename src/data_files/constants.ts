import ogImageSrc from "@images/social.png";



export const SITE = {
  title: "Trade Guild Consulting",
  tagline: "Business Challenges? We've Got You Covered.",
  description: "Trade Guild Consulting offers expert marketing, business consulting, social media management, SEO, and digital marketing services. Our MBA-level expertise helps businesses overcome challenges and achieve sustainable growth.",
  description_short: "Expert consulting services in marketing, business strategy, social media, SEO, and digital marketing.",
  url: "https://tradeguildconsulting.com",
  author: "Trade Guild Consulting",
};

export const SEO = {
  title: SITE.title,
  description: SITE.description,
  structuredData: {
    "@context": "https://schema.org",
    "@type": "ProfessionalService",
    inLanguage: "en-US",
    "@id": SITE.url,
    url: SITE.url,
    name: SITE.title,
    description: SITE.description,
    serviceType: ["Business Consulting", "Marketing Services", "Social Media Management", "SEO Services", "Digital Marketing"],
    isPartOf: {
      "@type": "WebSite",
      url: SITE.url,
      name: SITE.title,
      description: SITE.description,
    },
  },
};

export const OG = {
  locale: "en_US",
  type: "website",
  url: SITE.url,
  title: `${SITE.title}: Expert Business Consulting & Marketing Services`,
  description: "Transform your business with Trade Guild Consulting's expert services. From strategic marketing to business consulting, social media management, SEO, and digital marketing - we deliver MBA-level expertise and measurable results.",
  image: ogImageSrc,
};

export const CONTACT = {
  email: "connect@tradeguildconsulting.com",
};

export const ANALYTICS = {
  measurementId: "G-EZSRET9KZT",
};

export const partnersData = []

export const FEATURE_FLAGS = {
  showNewsletter: false,
  showContactForm: false,
};
